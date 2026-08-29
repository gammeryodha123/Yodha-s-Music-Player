[app]

# (str) Title of your application
title = Yodha's Music Player

# (str) Package name
package.name = yodhasmusicplayer

# (str) Package domain (needed for android packaging)
package.domain = org.yodha

# (str) Source code where app.py lives
source.dir = .

# (str) Source files to include
source.include_exts = py,png,jpg,kv,atlas,html,js,css

# (str) Application entry point
source.main = app.py

# (str) Application version
version = 1.0

# (str) Path to application icon
icon.filename = 1787932743309~2.jpg

# (list) Application requirements
# Note: yt-dlp is specified via pip/pure-python to prevent build failures
requirements = python3,kivy,flask,requests,certifi,urllib3,idna,charset-normalizer,yt-dlp

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) Use AndroidX support library
android.androidx = True

# (str) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (str) Path to build artifact storage
bin_dir = ./bin
