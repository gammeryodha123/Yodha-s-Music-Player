[app]

# (str) Title of your application
title = Yodha's Music Player

# (str) Package name
package.name = yodhasmusicplayer

# (str) Package domain (needed for android/ios packaging)
package.domain = com.yodha.musicplayer

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (include html/css/js files)
source.include_exts = py,png,jpg,kv,atlas,html,css,js

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,flask,yt-dlp,requests,urllib3,chardet,idna,certifi

# (list) Supported orientations
orientation = portrait

# OSX Specific
osx.kivy_version = 2.2.0

# Android specific
fullscreen = 0

# (list) Permissions needed for audio streaming & background playback
android.permissions = INTERNET, WAKE_LOCK, FOREGROUND_SERVICE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. Should match android.minapi.
android.ndk_api = 24

# (bool) Indicate whether the screen should stay on for audio playing
android.wakelock = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature
android.allow_backup = True

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2
ios.codesign.allowed = false

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

