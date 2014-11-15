dpath
=====

Simple library for querying nested dictionaries with a
very simple selector syntax instead of hardcoding the
paths. For example, given the data:

```python
nested = {
    'object': {
       'name': 'Eugene',
       'type': 'Person',
       'repos': ['repo1', 'repo2', 'repo3'],
       'events': [{
          'type': 'repo.commit',
          'time': '2014-10-25 18:32:11.314580',
        }],
    }
}
```

You can perform the following queries against the data:

```python
from dpath import get, update

get(nested, 'object.name')
get(nested, 'object.events[0].type')
get(nested, 'object.(name,type)')
get(nested, 'object.(events[0],name)')
```
