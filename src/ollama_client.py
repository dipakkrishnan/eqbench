from openai import OpenAI, ChatCompletion

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    # required but ignored
    api_key="ollama",
)


def generate_completion(prompt: str, model: str = "deepseek-r1") -> ChatCompletion:
    return client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}",
            }
        ],
        model=model,
    )
