from re import Scanner


scanner = Scanner([
    (r'\(',  lambda sc, token: ('BEGIN-BRACE', token)),
    (r'\)',  lambda sc, token: ('END-BRACE', token)),
    (r'\[',  lambda sc, token: ('BEGIN-NUM', token)),
    (r'\]',  lambda sc, token: ('END-NUM', token)),
    (r'\,',  lambda sc, token: ('SEP', token)),
    (r'\w+', lambda sc, token: ('KEY', token)),
    (r'\.',  lambda sc, token: None),
])


class LinkedScope(object):
    def __init__(self):
        self.stack = [[]]

    @property
    def top(self):
        return self.stack[-1]

    def push(self):
        top = []
        self.stack[-1].append(top)
        self.stack.append(top)
        return top

    def pop(self):
        self.stack.pop()

    def reduce_all(self):
        self.stack = [self.stack[0]]


def radify(tokens):
    mode = str
    stack = LinkedScope()
    for name, text in tokens:
        if name == 'BEGIN-NUM':
            mode = int

        elif name == 'END-NUM':
            mode = str

        elif name == 'BEGIN-BRACE':
            stack.push()  # one for all patterns
            stack.push()  # one for the current pattern

        elif name == 'SEP':
            stack.pop()   # pop the current pattern
            stack.push()  # push another pattern

        elif name == 'END-BRACE':
            stack.reduce_all()

        elif name =='KEY':
            stack.top.append(mode(text))
    return stack.top


def compile_selector(query):
    if isinstance(query, list):
        return query
    path, _ = scanner.scan(query)
    return list(radify(path))
