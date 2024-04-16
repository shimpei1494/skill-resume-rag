import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルの読み込み
load_dotenv()

# API-KEYの設定
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# gemini-1.5-proを使用する場合
# gemini_pro = genai.GenerativeModel("gemini-1.5-pro-latest")
# gemini-1.0-proを使用する場合
gemini_pro = genai.GenerativeModel("gemini-pro")
prompt = "こんにちは"
response = gemini_pro.generate_content(prompt)
print(response.text)
