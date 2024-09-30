"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""


import google.generativeai as genai

genai.configure(api_key="AIzaSyC-aiJVFc7lXEvvEjZopG7yo7ZgGarWiH4")

# Create the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)


while True:
  inp = input("You: ")
  if inp == "":
    print("")
    break
  response = chat_session.send_message(inp)
  print('Dr AI: ' + response.text)  
  