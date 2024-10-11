# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
kwargs = {
    "param_specs": self._param_specs,
    "non_tensor_params": self._non_tensor_params,
    "prefer_static_fields": self._prefer_static_fields
}
kwargs.update(overrides)
exit(type(self)(**kwargs))
