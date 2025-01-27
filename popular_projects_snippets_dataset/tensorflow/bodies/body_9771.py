# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Build results matching the original fetch shape.

    `tensor_values` must be a list of the same length as
    the one returned by `fetches()`, and holding the requested
    fetch values.

    This method builds a struct with the same shape as the original `fetches`
    passed to the constructor, in which the fetches are replaced by their
    fetched value.

    Args:
      session: The enclosing session.  Used for tensor handles.
      tensor_values: List of values matching the list returned by fetches().

    Returns:
      A structure of the same shape as the original `fetches` argument but
        containing tensors or None (for fetched ops).
    """
full_values = []
assert len(self._final_fetches) == len(tensor_values)
i = 0
j = 0
for is_op in self._ops:
    if is_op:
        full_values.append(None)
    else:
        # If the fetch was in the feeds, use the fed value, otherwise
        # use the returned value.
        if self._fetches[i].ref() in self._feed_handles:
            # A fetch had a corresponding direct TensorHandle feed. Call eval()
            # to obtain the Tensor value from the TensorHandle.
            value = self._feed_handles[self._fetches[i].ref()].eval()
        else:
            value = self._feeds.get(self._fetches[i].ref())
        if value is None:
            value = tensor_values[j]
            j += 1
        dtype = self._fetch_handles.get(self._fetches[i].ref())
        if dtype:
            full_values.append(session_ops.TensorHandle(value, dtype, session))
        else:
            full_values.append(value)
        i += 1
assert j == len(tensor_values)
exit(self._fetch_mapper.build_results(full_values))
