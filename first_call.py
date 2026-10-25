from dotenv import load_dotenv
import anthropic
import os

# key = os.getenv("ANTHROPIC_API_KEY")
# print("Key loaded:", key is not None)
# print("Starts with:", key[:7] if key else None, "| length:", len(key) if key else 0)

load_dotenv(override=True)
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=300,
    messages=[{"role": "user", "content": "Explain RAG to a tester in 3 lines."}],
)

print(response.content[0].text)
print("tokens in/out", response.usage.input_tokens, response.usage.output_tokens)