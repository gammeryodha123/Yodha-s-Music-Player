from flask import Flask, request, jsonify, render_template, Response
import yt_dlp, requests
import urllib.parse

app = Flask(__name__)

ydl_search = {'quiet': True, 'skip_download': True, 'extract_flat': True}
ydl_play = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'extractor_args': {'youtube': {'player_client': ['android']}}
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search-page')
def search_page():
    return render_template('search.html')

@app.route('/recent-page')
def recent_page():
    return render_template('recent.html')

@app.route('/playlists-page')
def playlists_page():
    return render_template('playlists.html')

@app.route('/downloads-page')
def downloads_page():
    return render_template('downloads.html')

@app.route('/search')
def search():
    q = request.args.get('q')
    if not q:
        return jsonify([])
    with yt_dlp.YoutubeDL(ydl_search) as ydl:
        res = ydl.extract_info(f"ytsearch10:{q}", download=False)
        songs = [{'title': e.get('title'), 'url': e.get('url'), 'id': e.get('id')} for e in res.get('entries', [])]
    return jsonify(songs)

@app.route('/play')
def play():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL missing'}), 400
        
    with yt_dlp.YoutubeDL(ydl_play) as ydl:
        info = ydl.extract_info(url, download=False)
        stream_url = info.get('url')
        
    encoded_stream_url = urllib.parse.quote(stream_url)
    return jsonify({
        'stream_url': f"/stream?url={encoded_stream_url}",
        'title': info.get('title')
    })

@app.route('/stream')
def stream():
    u = request.args.get('url')
    if not u:
        return "Missing stream URL", 400

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'https://www.youtube.com/'
    }
    r = requests.get(u, headers=headers, stream=True)

    def generate():
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                yield chunk

    content_type = r.headers.get('Content-Type', 'audio/webm')
    return Response(
        generate(),
        content_type=content_type,
        headers={'Accept-Ranges': 'bytes', 'Access-Control-Allow-Origin': '*'}
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
