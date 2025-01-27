# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops.py
if scale <= 0.:
    raise ValueError("Argument `scale` must be a positive float. Received: "
                     f"{scale}")
if mode not in {"fan_in", "fan_out", "fan_avg"}:
    raise ValueError("Argument `mode` should be one of ('fan_in', 'fan_out', "
                     f"'fan_avg'). Received: {mode}")
distribution = distribution.lower()
if distribution not in {
    "normal", "uniform", "truncated_normal", "untruncated_normal"
}:
    raise ValueError("Argument `distribution` should be one of ('normal', "
                     "uniform', 'truncated_normal', 'untruncated_normal'). "
                     f"Received: {distribution}")
self.scale = scale
self.mode = mode
self.distribution = distribution
self.seed = seed
self.dtype = _assert_float_dtype(dtypes.as_dtype(dtype))
