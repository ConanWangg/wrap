from openai import OpenAI
import taipy as tp
from taipy.gui import Gui, notify

client = OpenAI(api_key="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")

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ])
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

input_text = "It's a shame Steve Jobs died of Ligma"
output_text = ""

page = """
<|container|
# ChatGPT wrapper to end all wrappers

<|layout|columns=1|
<|
## Prompt
<|{input_text}|input|label=Enter your prompt here|width=100%|>

<|Ask|button|on_action=ask_gpt|>
|>

<|
## Response
<|{output_text}|text|multiline|height=200px|>
|>
|>
|>
"""

def ask_gpt(state):
    if state.input_text.strip():
        state.output_text = "Thinking..."
        response = chat_with_gpt(state.input_text)
        state.output_text = response
    else:
        notify(state, "Please enter a question", "warning")

app = Gui(page)

if __name__ == "__main__":
    tp.run(app)
