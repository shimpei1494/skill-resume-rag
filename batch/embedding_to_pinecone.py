import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from pinecone import Pinecone

# 環境変数をロード
load_dotenv()

# Azure OpenAIの設定
aoai_api_key = os.environ["AZURE_OPENAI_API_KEY"]
aoai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
client = AzureOpenAI(
    api_key=aoai_api_key,
    api_version="2024-02-01",
    azure_endpoint=aoai_endpoint
)

# Pineconeの設定
pinecone_api_key = os.environ["PINECONE_API_KEY"]
pinecone_index_name = os.environ["PINECONE_INDEX"]
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index(pinecone_index_name)

# 技術経歴書のテキストを読み込む
file_path = "skill_sheet/text/技術経歴書_深山颯斗.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text_content = file.read()

# テキストをembedding
response = client.embeddings.create(
    input=text_content,
    model="text-embedding-3-small",
    dimensions=512
)

# ベクトル配列を取得
embedding_vector = response.data[0].embedding

# Pineconeにアップロード
index.upsert(
    vectors=[
        {
            "id": "7",
            "values": embedding_vector,
            "metadata": {"filename": "技術経歴書_深山颯斗.txt", "username": "技術経歴書_深山颯斗.txt"}
        }
    ]
)

print(embedding_vector)
print("技術経歴書のembeddingがPineconeに保存されました。")