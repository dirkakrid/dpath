from dpath.path import compile_selector


def recurse(indexes, rc):
    for idx in indexes:
        stack = []
        for datum in rc:
            if isinstance(idx, list):
                for index in idx:
                    process = recurse((index,), rc=(datum,))
                    stack.extend(process)
                continue
            stack.append(datum[idx])
        rc[:] = stack
    return rc


def get(path, data):
    path = compile_selector(path)
    return recurse(path, [data])


def update(path, data, callback):
    path = compile_selector(path)
    for item in recurse(path, [data]):
        callback(item)
