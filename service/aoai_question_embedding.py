import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# 環境変数をロード
load_dotenv()

# 質問をembeddingしてベクトル配列を返す
def aoai_question_embedding(question: str):
    # Azure OpenAIの設定
    aoai_api_key = os.environ["AZURE_OPENAI_API_KEY"]
    aoai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
    client = AzureOpenAI(
        api_key=aoai_api_key,
        api_version="2024-02-01",
        azure_endpoint=aoai_endpoint
    )

    # テキストをembedding
    response = client.embeddings.create(
        input=question,
        model="text-embedding-3-small",
        dimensions=512
    )

    # ベクトル配列を取得
    embedding_vector = response.data[0].embedding

    print("質問のベクトル化---------------")
    print(embedding_vector)
    return embedding_vector