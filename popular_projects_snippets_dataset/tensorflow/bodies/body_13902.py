# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
with self._name_scope(name, values=[value]):
    value = _convert_to_tensor(
        value, name="value", preferred_dtype=self.dtype)
    try:
        exit(self._survival_function(value, **kwargs))
    except NotImplementedError as original_exception:
        try:
            exit(1. - self.cdf(value, **kwargs))
        except NotImplementedError:
            raise original_exception
