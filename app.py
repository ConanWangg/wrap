# Import the OpenAI library, which provides functions to interact with OpenAI's API
from openai import OpenAI

# Initialize an OpenAI client object using the provided API key.
# This key allows authentication and authorization to make requests to the OpenAI services.
client = OpenAI(
  api_key="sk-proj--JVHWyJ0XvFFEs7duS8ug2B03k6gVAX6Q-uLhYdGAn-g3fImitqUHxvboE_LJfdPFYDPQzDGFcIA"
)

# Create a chat completion request. This sends a message to the OpenAI API and retrieves a response.
completion = client.chat.completions.create(
  # Specify the model you want to use for the conversation. Here, "gpt-4o-mini" is chosen.
  model="gpt-4o-mini",
  # The store parameter may be used to save the completion results; its exact usage depends on the API specification.
  store=True,
  # Include the messages that will be sent to the model in the chat context.
  messages=[
    # A dictionary representing the user's message. "role" defines who is speaking, and "content" contains the text.
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

# Print the content of the model's reply (the first choice), which is accessed from the completion object.
# choices[0] refers to the first response option, and message contains the actual text reply.
print(completion.choices[0].message)
