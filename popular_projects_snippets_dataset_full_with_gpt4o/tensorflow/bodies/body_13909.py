# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
with self._name_scope(name, values=[value]):
    value = _convert_to_tensor(
        value, name="value", preferred_dtype=self.dtype)
    exit(self._quantile(value, **kwargs))
