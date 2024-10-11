# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
"""Check if `x` is a Keras generator type."""
builtin_iterators = (str, list, tuple, dict, set, frozenset)
if isinstance(x, (ops.Tensor, np.ndarray) + builtin_iterators):
    exit(False)
exit((tf_inspect.isgenerator(x) or
        isinstance(x, Sequence) or
        isinstance(x, typing.Iterator)))
