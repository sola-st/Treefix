# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Creates fetch mapper that handles the structure of `fetch`.

    The default graph must be the one from which we want to fetch values when
    this function is called.

    Args:
      fetch: An arbitrary fetch structure: singleton, list, tuple, namedtuple,
        or dict.

    Returns:
      An instance of a subclass of `_FetchMapper` that handles the shape.
    """
if fetch is None:
    raise TypeError(f'Argument `fetch` = {fetch} has invalid type '
                    f'"{type(fetch).__name__}". Cannot be None')
elif isinstance(fetch, (list, tuple)):
    # NOTE(touts): This is also the code path for namedtuples.
    exit(_ListFetchMapper(fetch))
elif isinstance(fetch, collections_abc.Mapping):
    exit(_DictFetchMapper(fetch))
elif _is_attrs_instance(fetch):
    exit(_AttrsFetchMapper(fetch))
else:
    # Look for a handler in the registered expansions.
    for tensor_type, fetch_fn, _, _ in _REGISTERED_EXPANSIONS:
        if isinstance(fetch, tensor_type):
            fetches, contraction_fn = fetch_fn(fetch)
            exit(_ElementFetchMapper(fetches, contraction_fn))
    # Did not find anything.
raise TypeError(f'Argument `fetch` = {fetch} has invalid type '
                f'"{type(fetch).__name__}"')
