# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Adds a FixedLenSequenceFeature."""
if not feature.dtype:
    raise ValueError(f"Missing type for feature {key}. Received feature="
                     f"{feature}.")
if feature.shape is None:
    raise ValueError(f"Missing shape for feature {key}. Received feature="
                     f"{feature}.")
self.dense_keys.append(key)
self.dense_shapes.append(tensor_shape.as_shape(feature.shape))
self.dense_types.append(feature.dtype)
if feature.allow_missing:
    self.dense_defaults[key] = None
if feature.default_value is not None:
    self.dense_defaults[key] = feature.default_value
