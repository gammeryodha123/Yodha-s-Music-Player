[app]

title = Yodha's Music Player
package.name = yodhasmusicplayer
package.domain = org.yodha

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css
source.main = main.py

version = 1.0
icon.filename = 1787932743309~2.jpg

requirements = python3,kivy,flask,requests,certifi,urllib3,idna,charset-normalizer,yt-dlp

orientation = portrait
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.androidx = True
android.archs = arm64-v8a, armeabi-v7a

# ADD THIS LINE TO FIX THE ERROR
android.accept_sdk_license = True

[buildozer]
log_level = 2
bin_dir = ./bin
