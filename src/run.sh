#!/bin/bash

if ! [[ -v API_TOKEN ]]; then
    echo "API token not set, please do step 1"
    exit 1
fi

version='[Main]'
if (( ARCHIVE )); then
    version='[Archive]'
fi

cd /content

if [ "$version" == "[Main]" ]; then
  git clone "https://github.com/Docile-Alligator/Infinity-For-Reddit"
else
  wget --output-file=Infinity.zip "https://github.com/Docile-Alligator/Infinity-For-Reddit/archive/refs/tags/v7.0.0.zip" 
  unzip "Infinity.zip"
  mv -T Infinity-For-Reddit-* Infinity-For-Reddit
fi

wget -P /content/ "https://github.com/TanukiAI/Infinity-keystore/raw/main/Infinity.jks"

python3 change_token.py

cd Infinity-For-Reddit/
./gradlew assembleRelease

mv /content/Infinity-For-Reddit/app/build/outputs/apk/release/app*.apk /app/output/Infinity.apk

