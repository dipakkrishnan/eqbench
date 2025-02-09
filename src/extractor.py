from openai import ChatCompletion


class Extractor:

    def __init__(self, completion: ChatCompletion):
        self.completion = completion
        self.content = self.completion.choices[0].message.content

    def extract_reasoning(self):
        try:
            start_tag = self.content.find("<think>")
            end_tag = self.content.find("</think>")

            if start_tag != -1 and end_tag != -1 and start_tag < end_tag:
                content = self.content[start_tag + len("<think>") : end_tag].strip()
                return content
            return None

        except Exception as e:
            print(f"Error parsing think tags: {e}")
            return None

    def extract_answer(self):
        start = self.content.find("\\boxed{") + len("\\boxed{")
        end = self.content.find("}", start)

        if start > len("\\boxed{") - 1 and end != -1:
            return self.content[start:end]
        return None


from ollama_client import generate_completion

completion = generate_completion("what is 2+2?")
dp = Extractor(completion)
print(dp.extract_reasoning())
print(dp.extract_answer())
