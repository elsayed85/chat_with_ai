import argparse
import json
import os

class Chat():
  def __init__(self, prompt=None):
    self.log = "" if prompt is None else f"{prompt}\n"

  def send(self, message, speaker):
    self.log += f"{speaker}: {message}\n"

  def generate(self, speaker, prior=None):
    prompt=f"{self.log}{speaker}:" if prior is None else f"{self.log}{prior}\n{speaker}:"
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt,
      temperature=1.4,
      max_tokens=256,
      stop="\n",
    )
    output = response["choices"][0]["text"].strip()
    if output != "":
      self.log += f"{speaker}: {output}\n"

  def save(self, filename):
    with open(filename, "w") as f:
      f.write(self.log)

if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument("-scene", default="omegle")
  parser.add_argument("-temp", type=float, default=1.4)
  args = parser.parse_args()

  if os.path.exists("api_key"):
    with open("api_key", "r") as f:
      openai.api_key = f.read()
  else:
    print("No API key found on file!")
    openai.api_key = input("Enter OpenAI API key: ")
    with open("api_key", "w") as f:
      f.write(openai.api_key)

  with open(f"scenes/{args.scene}.json") as f:
    scene = json.load(f)

  chat = Chat(prompt=scene["prompt"])

  done = False
  while not done:
    os.system("cls")
    print(chat.log)

    message = input(">")
    if message == "q":
      if not os.path.exists("logs"):
        os.makedirs("logs")
      name = input("Name this chat (or leave blank to discard):\n>")
      chat.save(f"logs/{name}.txt")
      done = True
    elif message == "":
      pass
    else:
      chat.send(message, speaker=scene["user"])

    if not done:
      chat.generate(speaker=scene["partner"], prior=scene["prior"])
