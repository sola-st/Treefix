# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Creates a _DictFetchMapper.

    Args:
      fetches: Dict of fetches.
    """
self._fetch_type = type(fetches)
if isinstance(fetches, collections.defaultdict):
    self._type_ctor = functools.partial(collections.defaultdict,
                                        fetches.default_factory)
else:
    self._type_ctor = self._fetch_type

self._keys = fetches.keys()
self._mappers = [
    _FetchMapper.for_fetch(fetch) for fetch in fetches.values()
]
self._unique_fetches, self._value_indices = _uniquify_fetches(self._mappers)
