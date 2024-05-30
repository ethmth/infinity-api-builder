FROM ubuntu:24.04

RUN apt-get --quiet update && apt-get --quiet install openjdk-11-jdk python3 python3-pip wget curl unzip git -y

WORKDIR /content

RUN wget --quiet --output-document=android-sdk.zip https://dl.google.com/android/repository/commandlinetools-linux-7583922_latest.zip
RUN unzip -q android-sdk.zip -d android-sdk

ENV ANDROID_SDK_ROOT="/content/android-sdk"
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
ENV PATH="${PATH}:/content/android-sdk/tools/bin:/content/android-sdk/platform-tools:/content/android-sdk/cmdline-tools/bin"

RUN bash /content/android-sdk/cmdline-tools/bin/sdkmanager --sdk_root=$ANDROID_SDK_ROOT "platforms;android-34" "build-tools;34.0.0"

RUN yes | sdkmanager --sdk_root=/content/android-sdk --licenses

COPY src .

CMD ["bash","run.sh"]
