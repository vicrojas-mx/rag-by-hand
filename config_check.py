import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("MY_API_KEY")
print("Key Loaded:", key is not None)
print("Starts with:", key[:4] if key else None)
