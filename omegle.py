# command line chatbot built with OpenAI API

import os
import requests

with open("api_key.txt", "r") as f:
  api_key = f.read()

print(api_key)

# main chat loop

interests = input("Enter some interests: ")
chatlog = f"You are now chatting with a random stranger.\nYou both like {interests}.\n"

while True:
  os.system("cls")
  print(chatlog)

  message = input(">")

  chatlog += f"You: {message}\n"

  prompt = chatlog + "Stranger:"

  # fetch gpt3 response
  response = requests.post(
    "https://api.openai.com/v1/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={
      "model": "text-davinci-003",
      "prompt": prompt,
      "temperature": 1.2,
      "max_tokens": 64,
      "stop": "\n",
    },
  )
  r = response.json()
  output = r["choices"][0]["text"]

  chatlog += f"Stranger:{output}\n"

