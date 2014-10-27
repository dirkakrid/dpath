from dpath.path import compile_selector


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


def get(path, data):
    return recurse(compile_selector(path), [data])
