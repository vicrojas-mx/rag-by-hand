class Step:
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        return Step(lambda x: other.func(self.func(x)))

    def invoke(self, x):
        return self.func(x)

prompt = Step(lambda q: f"Question: {q}")
llm = Step(lambda p: p + " -> Refunds take 5 days")
parser = Step(lambda r: r.upper())
chain = prompt | llm | parser

print(chain.invoke("how long for refunds?"))