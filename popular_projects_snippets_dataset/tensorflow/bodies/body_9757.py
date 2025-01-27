# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Creates a _ListFetchMapper.

    Args:
      fetches: List, tuple, or namedtuple of fetches.
    """
if isinstance(fetches, wrapt.ObjectProxy):
    self._fetch_type = type(fetches.__wrapped__)
else:
    self._fetch_type = type(fetches)
self._mappers = [_FetchMapper.for_fetch(fetch) for fetch in fetches]
self._unique_fetches, self._value_indices = _uniquify_fetches(self._mappers)
