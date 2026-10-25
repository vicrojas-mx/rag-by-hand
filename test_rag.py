import pytest

from rag import ask

def test_answers_from_context():
    assert "5 business days" in ask("How long refunds take", "refunds")

@pytest.mark.parametrize("question, keyword", [("Do you ship to Mexico?", "ship"), 
                                               ("When can I call support", "phone"),])
def test_says_i_dont_know_when_answer_is_missing(question, keyword):
    assert(ask(question, keyword).strip() == "I don't know.")