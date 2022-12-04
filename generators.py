import requests

class Generator():
  def __init__(self, api_key):
    self.api_key = api_key

class OpenAIGenerator(Generator):
  def generate(self, model="text-davinci-003", **kwargs):
    response = requests.post(
      "https://api.openai.com/v1/completions",
      headers={"Authorization": f"Bearer {self.api_key}"},
      json={"model": model, **kwargs},
    )
    r = response.json()
    try:
      return r["choices"][0]["text"]
    except:
      print(r)

  def edit(self, instruction, model="text-davinci-edit-001"):
    response = requests.post(
      "https://api.openai.com/v1/completions",
      headers={"Authorization": f"Bearer {self.api_key}"},
      json={"model": model, "instruction": instruction, **kwargs},
    )
    r = response.json()
    try:
      return r["choices"][0]["text"]
    except:
      print(r)

