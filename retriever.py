class Document:
    def __init__(self, content: str, metadata: dict | None = None) -> None:
        self.content = content
        if metadata == None:
            metadata = {}
        self.metadata = metadata

    def __repr__(self) -> str:
        return f"Document(content={self.content[:30]!r}, metadata={self.metadata})"

class Retriever:
    def __init__(self) -> None:
        self.documents: list[Document] = []

    def add(self, doc:Document) -> None:
        self.documents.append(doc)

    def search(self, query:str) -> list[Document]:
        result = []
        for document in self.documents:
            if query in document.content:
                result.append(document)
        return result
    
class CaseInsensitiveRetriever(Retriever):

    def search(self, query: str) -> list[Document]:        
        return [document for document in self.documents if query.lower() in document.content.lower()]

if __name__== "__main__":
    r = Retriever()
    r.add(Document("Refunds take 5 business days.", {'source': 'faq.txt'}))
    r.add(Document("Shipping is free over $50.", {'source': 'faq.txt'}))
    print(r.search("Refunds"))
    print(r.search("refuns"))

    print("---------------")
    ci = CaseInsensitiveRetriever()
    ci.add(Document("Refunds take 5 business days.", {"source": "faq.txt"}))
    print(ci.search("refunds"))
    print(ci.search("REFUNDS"))