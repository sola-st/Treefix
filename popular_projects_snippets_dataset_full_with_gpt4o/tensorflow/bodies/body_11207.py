# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
if scale <= 0.:
    raise ValueError("Argument `scale` must be a positive float. Received: "
                     f"{scale}")
if mode not in {"fan_in", "fan_out", "fan_avg"}:
    raise ValueError("Argument `mode` should be one of ('fan_in', 'fan_out', "
                     f"'fan_avg'). Received: {mode}")
distribution = distribution.lower()
# Compatibility with keras-team/keras.
if distribution == "normal":
    distribution = "truncated_normal"
if distribution not in {"uniform", "truncated_normal",
                        "untruncated_normal"}:
    raise ValueError("Argument `distribution` should be one of ('uniform', "
                     "'truncated_normal', 'untruncated_normal'). Received: "
                     f"{distribution}")
self.scale = scale
self.mode = mode
self.distribution = distribution
self.seed = seed
self._random_generator = _RandomGenerator(seed)
