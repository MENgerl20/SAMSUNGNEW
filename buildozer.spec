[app]

# (str) Title of your application
title = Samsung Optimizer

# (str) Package name
package.name = samsungoptimizer

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd,pillow,openssl

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
android.presplash_color = #000000

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.io/lottie/
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at least)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (bool) Accept SDK license agreements automatically
# android.accept_sdk_license = False
android.accept_sdk_license = True

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (str) Android additional adb arguments
#android.adb_args = -H 10.0.0.1

# (list) Android-specific build dependencies and options
#android.gradle_dependencies = com.google.firebase:firebase-ads:10.2.0

# (list) Java classes to add to the compilation
#android.add_jars = foo.jar,bar.jar,common/android.jar

# (list) Java files to add to the android project (can be java or a directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory
#android.add_assets =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx = True

# (list) Add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for more information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes 
# e.g. android.gradle_repositories = "maven { url 'https://jitpack.io' }"
#android.gradle_repositories =

# (list) Packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# please enclose in double quotes 
# e.g. android.packaging_options = "pickFirst 'lib/*/libllvm_for_mono.so'"
#android.packaging_options =

# (list) Java classes to exclude from the compilation
#android.skip_update_options =

# (str) The format used to package the app for release mode (aab or apk or aar).
#android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
#android.debug_artifact = apk

#
# Python for android (p4a) specific
#

# (str) python-for-android fork to use, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android local directory to use instead of clone
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) Port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port =

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
# "in the future" --use-setup-py will be the default behavior in p4a, however
# right now it is not so, this just enables it.
#p4a.setup_py = false

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
#p4a.extra_args =


#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: security find-identity -v -p codesigning
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s


#
# Mac OS X specific
#

# (str) Kivy version to use
osx.kivy_version = 2.3.0

# (str) python-for-android fork to use, defaults to upstream (kivy)
#osx.python_version = 3

# (str) python-for-android branch to use, defaults to master
#osx.kivy_ios_url = https://github.com/kivy/kivy-ios

# (str) python-for-android local directory to use instead of clone
#osx.kivy_ios_branch = master

# (list) The modules to exclude from the build
#osx.exclude_patterns = license,images/*/*.jpg

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#osx.frameworks = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#osx.resources = 


#
# Windows specific
#

# (str) Kivy version to use
#win.kivy_version = 2.3.0

# (str) python-for-android fork to use, defaults to upstream (kivy)
#win.python_version = 3

# (str) python-for-android branch to use, defaults to master
#win.kivy_windows_url = https://github.com/kivy/kivy-windows

# (str) python-for-android local directory to use instead of clone
#win.kivy_windows_branch = master

# (list) The modules to exclude from the build
#win.exclude_patterns = license,images/*/*.jpg

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#win.libs = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#win.resources = 


#
# CI specific
#

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#ci.branch = master

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#ci.root = .
