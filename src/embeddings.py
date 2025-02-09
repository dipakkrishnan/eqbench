import os
import openai
import numpy

client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_embeddings(input_text: list[str], model: str = "text-embedding-3-small"):
    response = client.embeddings.create(
        model=model, input=input_text
    )
    return [data["embedding"] for data in response["data"]]
