import os

from pinecone import Pinecone
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pc.Index(os.environ["PINECONE_INDEX"])

# 全て要素の値が0.1の512次元のベクトル値
test_vector_values1= [0.1] * 512
# 全て要素の値が0.5の512次元のベクトル値
test_vector_values5 = [0.5] * 512

index.upsert(
    vectors=[
        {
            "id": "1",
            "values": test_vector_values1,
            "metadata": {"filename": "テスト太郎.pdf", "username": "テスト太郎"}
        },
        {
            "id": "5",
            "values": test_vector_values5,
            "metadata": {"filename": "５番目の男.pdf", "username": "5番目の男"}
        }
    ]
)

