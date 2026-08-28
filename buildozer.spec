[app]

# (str) Title of your application
title = Yodha's Music Player

# (str) Package name
package.name = yodhasmusicplayer

# (str) Package domain (needed for android packaging)
package.domain = org.yodha

# (str) Source files to include (let it default to all files in the directory)
source.include_exts = py,png,jpg,kv,atlas,html,js,css

# (str) Application entry point (using app.py as requested)
source.main = app.py

# (list) Application requirements
# Add your Python dependencies here (Flask, yt-dlp, requests)
requirements = python3,kivy,flask,yt-dlp,requests,certifi,urllib3,idna,charset-normalizer,idna

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Use a AndroidX support library
android.androidx = True

# (str) Supported architectures (arm64-v8a is standard for modern devices)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (str) Path to build artifact storage
bin_dir = ./bin
