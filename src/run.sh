#!/bin/bash

if ! [[ -v API_TOKEN ]]; then
    echo "API token not set, please do step 1"
    exit 1
fi

cd /content

if [ "$VERSION" == "" ]; then
  git clone "https://github.com/Docile-Alligator/Infinity-For-Reddit"
else
  git clone --depth 1 --branch $VERSION https://github.com/Docile-Alligator/Infinity-For-Reddit
fi

wget -P /content/ "https://github.com/TanukiAI/Infinity-keystore/raw/main/Infinity.jks"

python3 change_token.py

cd Infinity-For-Reddit/
./gradlew assembleRelease

mv /content/Infinity-For-Reddit/app/build/outputs/apk/release/app*.apk /app/output/Infinity.apk

