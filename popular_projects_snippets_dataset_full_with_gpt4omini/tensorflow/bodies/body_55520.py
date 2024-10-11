# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
def inner(values):
    for v in nest.flatten(values):
        if not (isinstance(v, expected_types) or
                (isinstance(v, np.ndarray) and
                 issubclass(v.dtype.type, expected_types))):
            _check_failed(v)

exit(inner)
