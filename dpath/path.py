from collections import deque
from re import Scanner


scanner = Scanner([
    (r'\(',     lambda sc, token: ('BEGIN-BRACE', token)),
    (r'\)',     lambda sc, token: ('END-BRACE', token)),
    (r'\[',     lambda sc, token: ('BEGIN-NUM', token)),
    (r'\]',     lambda sc, token: ('END-NUM', token)),
    (r'\,',     lambda sc, token: ('SEP', token)),
    (r'\w+',    lambda sc, token: ('KEY', token)),
    (r'\.',     lambda sc, token: None),
])


def radify(tokens):
    stack = [[]]
    modes = [str]
    while tokens:
        name, text = tokens.popleft()
        if name == 'BEGIN-NUM':
            modes.append(int)

        elif name == 'END-NUM':
            modes.pop()

        elif name == 'BEGIN-BRACE':
            root = [[]]
            stack[-1].append(root)
            stack.append(root)
            stack.append(root[0])

        elif name == 'SEP':
            stack.pop()
            root = stack[-1]
            this = []
            root.append(this)
            stack.append(this)

        elif name == 'END-BRACE':
            stack = stack[:1]

        elif name =='KEY':
            stack[-1].append(modes[-1](text))
    return stack[0]


def compile_selector(query):
    path, _ = scanner.scan(query)
    path = deque(path)
    return list(radify(path))
