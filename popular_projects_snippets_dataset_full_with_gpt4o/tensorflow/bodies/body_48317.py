# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
value = dtypes.as_dtype(value).name
self._set_dtype_policy(policy.Policy(value))
