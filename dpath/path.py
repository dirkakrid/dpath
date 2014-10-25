def numerical_indexes(item):
    while '[' in item:
        start, end = item.index('['), item.index(']')
        index = item[(start+1):end]
        yield int(index)
        item = item[(end+1):]


def indexes(text):
    for item in text.split('.'):
        if '[' in item:
            prefix = item.split('[')[0]
            if prefix:
                yield prefix
            for idx in numerical_indexes(item):
                yield idx
            continue
        yield item
