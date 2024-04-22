import os

from pinecone import Pinecone
from dotenv import load_dotenv

load_dotenv()

def query_search_pinecone(vector: list):
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
    index = pc.Index(os.environ["PINECONE_INDEX"])

    result = index.query(
        vector=vector,
        top_k=3, # 3件まで取得
        include_values=False, # values(ベクトル値)を含めるか
        include_metadata=True # metadataを含めるか
    )

    print("pinecone結果-----")
    print(result)
    print(result['matches'][0]['metadata']['filename'])

    return(result['matches'])

