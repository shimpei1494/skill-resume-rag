import os

from pinecone import Pinecone
from dotenv import load_dotenv

load_dotenv()

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pc.Index(os.environ["PINECONE_INDEX"])

# 全て要素の値が0.3の512次元のベクトル値
test_vector_values3 = [0.3] * 512

result = index.query(
    vector=test_vector_values3, # インデックス内のデータと比較するベクトル値
    top_k=2, # ランキング何番目まで取得するか
    include_values=False, # values(ベクトル値)を含めるか
    include_metadata=True # metadataを含めるか
)

print(result)