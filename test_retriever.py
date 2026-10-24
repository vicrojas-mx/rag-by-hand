import pytest
from retriever import Document, Retriever, CaseInsensitiveRetriever

def test_search_finds_matching_document():
    r = Retriever()
    r.add(Document("Refunds take 5 business days."))
    results = r.search("Refunds")
    assert(len(results) == 1)
    assert(results[0].content == "Refunds take 5 business days.")

def test_search_returns_empty_list_when_no_match():
    r = Retriever()
    r.add(Document("Refunds take 5 business days."))
    results = r.search("pizza")
    assert(results == [])


def test_search_is_case_sensitive():
    r = Retriever()
    r.add(Document("Refunds take 5 business days."))
    results = r.search("refunds")
    assert(results == [])

@pytest.mark.parametrize("query", ["refunds", "REFUNDS", "reFunds"])
def test_case_insensitive_finds_anycase_query(query):
    r = CaseInsensitiveRetriever()
    r.add(Document("Refunds take 5 business days."))
    results = r.search(query)
    assert(len(results) == 1)
    assert(results[0].content == "Refunds take 5 business days.")
