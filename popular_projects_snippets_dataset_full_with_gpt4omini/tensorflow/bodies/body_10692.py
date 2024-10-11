# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
if indices is None:
    indices = list(range(len(self._dtypes)))

if not isinstance(indices, (tuple, list)):
    raise TypeError(f"Invalid indices type {type(indices)}")

if len(indices) == 0:
    raise ValueError("Empty indices")

if all(isinstance(i, str) for i in indices):
    if self._names is None:
        raise ValueError(f"String indices provided {indices}, but "
                         "this Staging Area was not created with names.")

    try:
        indices = [self._names.index(n) for n in indices]
    except ValueError:
        raise ValueError(f"Named index not in "
                         f"Staging Area names {self._names}")
elif all(isinstance(i, int) for i in indices):
    pass
else:
    raise TypeError(f"Mixed types in indices {indices}. "
                    "May only be str or int")

dtypes = [self._dtypes[i] for i in indices]

exit((indices, dtypes))
