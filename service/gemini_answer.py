import os
from dotenv import load_dotenv
import google.generativeai as genai
from service.aoai_question_embedding import aoai_question_embedding
from service.query_search_pincone import query_search_pinecone

# .envファイルの読み込み
load_dotenv()

# API-KEYの設定
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

def gemini_answer(input: str):
    # 質問のベクトル化
    vector_list = aoai_question_embedding(input)
    # 検索
    search_result = query_search_pinecone(vector_list)
    # 技術経歴書のテキストを読み込む
    text_content = "# 指示\n以下の参考情報を参考に質問内容に答えてください。参考情報には名前とその人のエンジニアとしての経歴が書かれています。\n"
    text_content += "# 参考情報\n"
    for person in search_result:
        file_path = f"skill_sheet/text/{person['metadata']['filename']}"
        with open(file_path, "r", encoding="utf-8") as file:
            text_content += f"## {person['metadata']['username']}\n"
            text_content += file.read()
            text_content += "\n"
    text_content += "# 質問内容\n"
    text_content += input

    print(text_content)
    # 検索結果をプラスして質問投げる→回答返す
    gemini_pro = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = gemini_pro.generate_content(text_content)
    return response.text
    # return "hello"
