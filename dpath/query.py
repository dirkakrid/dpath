from dpath.path import compile_selector


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


def get(path, data):
    path = compile_selector(path)
    return recurse(path, [data])


def update(path, data, callback):
    path = compile_selector(path)
    for item in recurse(path, [data]):
        callback(item)
