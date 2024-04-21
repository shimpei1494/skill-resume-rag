import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()
aoai_api_key = os.environ["AZURE_OPENAI_API_KEY"]
aoai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]

client = AzureOpenAI(
    api_key = aoai_api_key,
    api_version = "2024-02-01",
    azure_endpoint = aoai_endpoint
)

response = client.embeddings.create(
    input = "Your text string goes here",
    model = "text-embedding-3-small",
    dimensions=512
)

print(response)
print(response.model_dump_json(indent=2))