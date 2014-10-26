from collections import deque, namedtuple
from re import Scanner


Token = namedtuple('Token', ('name', 'text'))
scanner = Scanner([
    (r'\(',    lambda sc, token: Token('BEGIN-BRACE', token)),
    (r'\)',    lambda sc, token: Token('END-BRACE', token)),
    (r'\[',    lambda sc, token: Token('BEGIN-NUM', token)),
    (r'\]',    lambda sc, token: Token('END-NUM', token)),
    (r'(\w+)', lambda sc, token: Token('KEY', token)),
    (r'[.,]',  lambda sc, token: None),
])


def radify(results, mode=str):
    while results:
        token = results.popleft()
        if token.name == 'END-BRACE':
            break
        elif token.name == 'BEGIN-NUM':
            mode = int
        elif token.name == 'END-NUM':
            mode = str
        elif token.name == 'BEGIN-BRACE':
            yield list(radify(results, mode))
        else:
            yield [mode(token.text)]


def compile_selector(query):
    if isinstance(query, list):
        return query
    results, _ = scanner.scan(query)
    results = deque(results)
    return radify(results)
