from pytest import fixture
from dpath.query import replace, get, update


@fixture
def nested():
    return {'object': {
            'name': 'Eugene',
            'type': 'Person',
            'repos': ['repo1', 'repo2', 'repo3'],
            'events': [{
                'type': 'repo.commit',
                'time': '2014-10-25 18:32:11.314580',
                }]}}


def test_get(nested):
    assert get('object.name', nested) == 'Eugene'
    assert get('object.events[0].type', nested) == 'repo.commit'


def test_update(nested):
    update('object.repos', nested, lambda x: x.append('repo4'))
    update('object.events', nested, lambda x: x.pop())
    assert nested['object']['repos'][-1] == 'repo4'
    assert not nested['object']['events']


def test_replace(nested):
    replace('object.events[0].type', nested, 'repo.destroy')
    replace('object.type', nested, 'Admin')
    assert nested['object']['events'][0]['type'] == 'repo.destroy'
    assert nested['object']['type'] == 'Admin'
