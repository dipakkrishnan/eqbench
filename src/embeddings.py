import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def generate_embeddings(text: str, model: str = "text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


def bulk(texts: list[str]):
    embeddings: list[list[float]] = []
    for text in texts:
        embeddings.append(generate_embeddings(text))
    return embeddings
