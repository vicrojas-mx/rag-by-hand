from dotenv import load_dotenv
import anthropic
from retriever import Document, CaseInsensitiveRetriever

load_dotenv(override=True)
client = anthropic.Anthropic()

r = CaseInsensitiveRetriever()
r.add(Document("Refunds take 5 business days.", {"source": "faq.txt"}))
r.add(Document("Shipping is free over 50.", {"source": "faq.txt"}))
r.add(Document("Support is open Monday to Friday, 9am to 5pm.", {"source": "faq.txt"}))

def ask(question:str, keyword:str) -> str:
    docs = r.search(keyword)
    context = "\n".join(d.content for d in docs)
    prompt = (f"Answer ONLY from this context. If the answer is not there, "
              f"reply with exactly: 'I don't know. \n\nContext:\n{context}\n\nQuestion: {question}")

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=200,
        messages=[{"role": "user", "content":prompt}]
    )
    return response.content[0].text

if __name__ == "__main__":
    print(ask("How long do refunds take?", "refunds"))
    print("1:", ask("Do you ship to Mexico?", "ship"))
    print("2:", ask("When can I call support?", "phone"))
    print("3:", ask("How long for my money back?", "money"))