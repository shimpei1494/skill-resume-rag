# TODO 動作未確認
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# APIキーを設定
api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)

# Embeddingを取得する関数を定義
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
        dimensions=512
    )
    return response

# テキストをEmbeddingに変換
text = "こんにちは、ChatGPT!"
embedding_result = get_embedding(text)
print("出力結果")
print(embedding_result)
print("次元数")
print(len(embedding_result["data"][0]["embedding"]))