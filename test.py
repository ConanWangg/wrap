from openai import OpenAI

client = OpenAI(
  api_key="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"
)

# Set your OpenAI API key

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",  # You can also use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ])
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
user_input = "What is the capital of France?"
response = chat_with_gpt(user_input)
print(response)
