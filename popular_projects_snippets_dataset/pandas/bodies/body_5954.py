# Extracted from ./data/repos/pandas/pandas/tests/extension/json/array.py
if isinstance(key, numbers.Integral):
    self.data[key] = value
else:
    if not isinstance(value, (type(self), abc.Sequence)):
        # broadcast value
        value = itertools.cycle([value])

    if isinstance(key, np.ndarray) and key.dtype == "bool":
        # masking
        for i, (k, v) in enumerate(zip(key, value)):
            if k:
                assert isinstance(v, self.dtype.type)
                self.data[i] = v
    else:
        for k, v in zip(key, value):
            assert isinstance(v, self.dtype.type)
            self.data[k] = v
