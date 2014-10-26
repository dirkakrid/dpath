from dpath.path import tokenise


def recurse(indexes, rc):
    for index in indexes:
        stack = []
        for datum in rc:
            if isinstance(index, str):
                stack.append(datum[index])
                continue
            for item in index:
                stack.extend(recurse(item, rc=[datum]))
        rc = stack
    return rc


def compile_selector(path):
    if isinstance(path, list):
        return path
    return list(tokenise(path))


def get(path, data):
    return recurse(compile_selector(path), [data])
