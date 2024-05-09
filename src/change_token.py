import os
import re

api_token = os.environ.get('API_TOKEN')
redirect_uri = os.environ.get('REDIRECT_URI')
your_reddit_username = os.environ.get('REDDIT_USERNAME')

user_agent = f"android:personal-app:0.0.1 (by /u/{your_reddit_username})"

# Change API
apiutils_file = "/content/Infinity-For-Reddit/app/src/main/java/ml/docilealligator/infinityforreddit/utils/APIUtils.java"

apiutils_code = open(apiutils_file, "r", encoding="utf-8-sig").read()
apiutils_code = apiutils_code.replace("NOe2iKrPPzwscA", api_token)
apiutils_code = apiutils_code.replace("infinity://localhost", redirect_uri)
apiutils_code = re.sub(r'public static final String USER_AGENT = ".*?";', f'public static final String USER_AGENT = "{user_agent}";', apiutils_code)

with open(apiutils_file, "w", encoding="utf-8") as f:
  f.write(apiutils_code)

build_gradle_file = "/content/Infinity-For-Reddit/app/build.gradle"
build_gradle_code = open(build_gradle_file, "r", encoding="utf-8-sig").read()
build_gradle_code = build_gradle_code.replace(r"""    buildTypes {""", r"""    signingConfigs {
        release {
            storeFile file("/content/Infinity.jks")
            storePassword "Infinity"
            keyAlias "Infinity"
            keyPassword "Infinity"
        }
    }
    buildTypes {""")
build_gradle_code = build_gradle_code.replace(r"""    buildTypes {
        release {""", r"""    buildTypes {
        release {
            signingConfig signingConfigs.release""")

with open(build_gradle_file, "w", encoding="utf-8") as f:
  f.write(build_gradle_code)
