[app]

# Title of your application
title = EA FC Team OVR Calculator

# Package name
package.name = team_ovr_calculator

# Package domain (needed for android/ios packaging)
package.domain = app.mrsheeko

# Source code directory where the main.py lives
source.dir = .

# Source files to include (let empty to include all the files)
source.include_exts = py

# Application version
version = 1.0

# Application requirements (Python and Kivy)
requirements = python3,kivy

# Icon of the application (replace 'icon.png' with the actual filename)
icon.filename = %(source.dir)s/icon.png

# Supported orientations (portrait in this case)
orientation = portrait

# Android specific settings
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET

# Minimum and target Android API levels
android.minapi = 21
android.api = 31

# Whether or not to use AndroidX
android.enable_androidx = True

# APK artifact format (apk for debug, aab for release)
android.debug_artifact = apk

# Add extra resources (e.g., images) to the assets directory
# android.add_assets =

# Add extra resources (e.g., images) to the res directory
# android.add_resources =

# Add Java .jar files to libs/armeabi
# android.add_jars =

# Add Java files to the android project
# android.add_src =

# Add Android AAR archives
# android.add_aars =
