# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Creates a _AttrsFetchMapper.

    Args:
      fetches: An instance of an attrs decorated class.
    """
values = _get_attrs_values(fetches)
self._fetch_type = type(fetches)
self._mappers = [_FetchMapper.for_fetch(fetch) for fetch in values]
self._unique_fetches, self._value_indices = _uniquify_fetches(self._mappers)
