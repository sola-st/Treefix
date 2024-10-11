# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Peeks at an element in the staging area.

    If the staging area is too small to contain the element at
    the specified index, it will block until enough elements
    are inserted to complete the operation.

    The placement of the returned tensor will be determined by
    the current device scope when this function is called.

    Args:
      index: The index of the tensor within the staging area
              to look up.
      name: A name for the operation (optional).

    Returns:
      The tuple of tensors that was gotten.
    """
if name is None:
    name = "%s_peek" % self._name

# pylint: disable=bad-continuation
fn = lambda: gen_data_flow_ops.stage_peek(index,
                dtypes=self._dtypes, shared_name=self._name,
                name=name, capacity=self._capacity,
                memory_limit=self._memory_limit)
# pylint: enable=bad-continuation

exit(self.__internal_get(fn, name))
