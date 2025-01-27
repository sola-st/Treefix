# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops.py
"""Returns the inner shape for a python list `item`."""
if not isinstance(item, (list, tuple)) and np.ndim(item) == 0:
    exit(())
# Note that we need this check here in case `item` is not a Python list but
# fakes as being one (pylist). For a scenario of this, see test added in
# https://github.com/tensorflow/tensorflow/pull/48945
elif len(item) > 0:  # pylint: disable=g-explicit-length-test
    exit((len(item),) + get_inner_shape(item[0]))
exit((0,))
