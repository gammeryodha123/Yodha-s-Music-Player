import os
import re
import urllib.parse
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
import yt_dlp
import requests

app = Flask(__name__)

# Options for yt_dlp extraction
YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'quiet': True,
    'no_warnings': True,
    'extract_flat': False,
    'nocheckcertificate': True,
}

@app.route('/')
def home():
    """Renders the main music player interface."""
    return render_template('index.html')

@app.route('/api/search', methods=['GET'])
def search_tracks():
    """Searches YouTube for tracks based on a query string."""
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({'error': 'Search query is required'}), 400

    search_url = f"ytsearch10:{query}"
    
    try:
        with yt_dlp.YoutubeDL(YTDL_OPTIONS) as ydl:
            info = ydl.extract_info(search_url, download=False)
            results = []
            
            for entry in info.get('entries', []):
                if entry:
                    results.append({
                        'id': entry.get('id'),
                        'title': entry.get('title'),
                        'uploader': entry.get('uploader'),
                        'duration': entry.get('duration'),
                        'thumbnail': entry.get('thumbnail'),
                    })
                    
            return jsonify({'status': 'success', 'results': results})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/stream/<video_id>', methods=['GET'])
def get_stream_info(video_id):
    """Retrieves direct audio stream URL and details for a given video ID."""
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    try:
        with yt_dlp.YoutubeDL(YTDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Select best audio format
            audio_url = None
            for fmt in info.get('formats', []):
                if fmt.get('acodec') != 'none' and fmt.get('vcodec') == 'none':
                    audio_url = fmt.get('url')
                    break
            
            if not audio_url:
                audio_url = info.get('url')

            return jsonify({
                'status': 'success',
                'title': info.get('title'),
                'artist': info.get('uploader'),
                'thumbnail': info.get('thumbnail'),
                'stream_url': audio_url
            })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/proxy')
def proxy_audio():
    """Proxies the raw audio stream to bypass CORS and access restrictions."""
    audio_url = request.args.get('url')
    if not audio_url:
        return jsonify({'error': 'Missing stream URL'}), 400

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    }

    req = requests.get(audio_url, headers=headers, stream=True)
    return Response(
        stream_with_context(req.iter_content(chunk_size=1024 * 8)),
        content_type=req.headers.get('Content-Type', 'audio/mpeg')
    )

if __name__ == '__main__':
    # Default host/port setup for local development and Android packaging
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
