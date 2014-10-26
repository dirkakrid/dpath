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

get('object.name', nested)
get('object.events[0].type', nested)
get('object.(name,type)', nested)
get('object.(events[0],name)')
```
