from dpath.path import indexes


def test_indexes():
    assert list(indexes('obj.this.that')) == ['obj', 'this', 'that']
    assert list(indexes('obj[0].this[1]')) == ['obj', 0 ,'this', 1]
    assert list(indexes('[0][1].that')) == [0, 1, 'that']
