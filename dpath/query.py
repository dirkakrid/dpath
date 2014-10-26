from dpath.path import tokenise


def recurse(indexes, rc):
    for index in indexes:
        stack = []
        for datum in rc:
            if isinstance(index, list):
                for item in index:
                    stack.extend(recurse(item, rc=[datum]))
                continue
            stack.append(datum[index])
        rc = stack
    return rc


def compile_selector(path):
    if isinstance(path, list):
        return path
    return list(tokenise(path))


def get(path, data):
    return recurse(compile_selector(path), [data])


def update(path, data, callback):
    for item in recurse(compile_selector(path), [data]):
        callback(item)
