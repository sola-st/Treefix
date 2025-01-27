# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
super(Metric, self).__init__(name=name, dtype=dtype, **kwargs)
self.stateful = True  # All metric layers are stateful.
self.built = True
if not base_layer_utils.v2_dtype_behavior_enabled():
    # We only do this when the V2 behavior is not enabled, as when it is
    # enabled, the dtype already defaults to floatx.
    self._dtype = (backend.floatx() if dtype is None
                   else dtypes.as_dtype(dtype).name)
