from dpath.path import indexes


def get(query, data):
    for index in indexes(query):
        data = data[index]
    return data


def update(query, data, callback):
    for index in indexes(query):
        data = data[index]
    callback(data)
    return data
