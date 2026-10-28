import os
import re

api_token = os.environ.get('API_TOKEN')
redirect_uri = os.environ.get('REDIRECT_URI')
your_user_agent = os.environ.get('USER_AGENT')
content_dir = os.environ.get('CONTENT_DIR', os.path.dirname(os.path.abspath(__file__)))

# Change API
apiutils_file = os.path.join(content_dir, "Infinity-For-Reddit/app/src/main/java/ml/docilealligator/infinityforreddit/utils/APIUtils.java")

apiutils_code = open(apiutils_file, "r", encoding="utf-8-sig").read()
apiutils_code = re.sub(
    r'public static final String CLIENT_ID = ".*?";',
    f'public static final String CLIENT_ID = "{api_token}";',
    apiutils_code,
)
apiutils_code = re.sub(
    r'public static final String REDIRECT_URI = ".*?";',
    f'public static final String REDIRECT_URI = "{redirect_uri}";',
    apiutils_code,
)
apiutils_code = re.sub(
    r'public static final String USER_AGENT = ".*?";',
    f'public static final String USER_AGENT = "{your_user_agent}";',
    apiutils_code,
)

with open(apiutils_file, "w", encoding="utf-8") as f:
  f.write(apiutils_code)

build_gradle_file = os.path.join(content_dir, "Infinity-For-Reddit/app/build.gradle")
build_gradle_code = open(build_gradle_file, "r", encoding="utf-8-sig").read()
build_gradle_code = build_gradle_code.replace(r"""    buildTypes {""", f"""    signingConfigs {{
        release {{
            storeFile file("{content_dir}/Infinity.jks")
            storePassword "Infinity"
            keyAlias "Infinity"
            keyPassword "Infinity"
        }}
    }}
    buildTypes {{""")
build_gradle_code = build_gradle_code.replace(r"""    buildTypes {
        release {""", r"""    buildTypes {
        release {
            signingConfig signingConfigs.release""")

with open(build_gradle_file, "w", encoding="utf-8") as f:
  f.write(build_gradle_code)
