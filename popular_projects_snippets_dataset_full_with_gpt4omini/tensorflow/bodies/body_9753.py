# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Creates an _ElementFetchMapper.

    This is the fetch mapper used for leaves in the fetch struct.  Because of
    the expansions mechanism, a leaf can actually fetch more than one tensor.

    Also note that the fetches here can be just strings (tensor or op names) or
    any other object that the graph knows how to convert to a tensor, such as a
    Variable.  So we have to run each fetch through `as_graph_element()` to get
    the corresponding tensor or op.

    Args:
      fetches: List of objects, as returned by a fetch_fn defined in
        _REGISTERED_EXPANSIONS.
      contraction_fn: Callable as returned by a fetch_fn.
    """
self._unique_fetches = []
for fetch in fetches:
    try:
        self._unique_fetches.append(ops.get_default_graph().as_graph_element(
            fetch, allow_tensor=True, allow_operation=True))
    except TypeError as e:
        raise TypeError(f'Argument `fetch` = {fetch} has invalid type '
                        f'"{type(fetch).__name__}" must be a string or Tensor. '
                        f'({str(e)})')
    except ValueError as e:
        raise ValueError(f'Argument `fetch` = {fetch} cannot be interpreted as '
                         f'a Tensor. ({str(e)})')
    except KeyError as e:
        raise ValueError(f'Argument `fetch` = {fetch} cannot be interpreted as '
                         f'a Tensor. ({str(e)})')
self._contraction_fn = contraction_fn
