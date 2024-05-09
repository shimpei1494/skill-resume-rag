# TODO 動作未確認
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# APIキーを設定
api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {
      "role": "user",
      "content": "こんにちは"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# テキストをEmbeddingに変換

print("出力結果")
print(response.choices[0].message.content)

