# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Adds a FixedLenFeature."""
if not feature.dtype:
    raise ValueError(f"Missing type for feature {key}. Received feature="
                     f"{feature}.")
if feature.shape is None:
    raise ValueError(f"Missing shape for feature {key}. Received feature="
                     f"{feature}.")
feature_tensor_shape = tensor_shape.as_shape(feature.shape)
if (feature.shape and feature_tensor_shape.ndims and
    feature_tensor_shape.dims[0].value is None):
    raise ValueError(f"First dimension of shape for feature {key} unknown. "
                     "Consider using FixedLenSequenceFeature. Received "
                     f"feature={feature}.")
if (feature.shape is not None and
    not feature_tensor_shape.is_fully_defined()):
    raise ValueError(f"All dimensions of shape for feature {key} need to be "
                     f"known but received {feature.shape!s}.")
self.dense_keys.append(key)
self.dense_shapes.append(tensor_shape.as_shape(feature.shape))
self.dense_types.append(feature.dtype)
if feature.default_value is not None:
    self.dense_defaults[key] = feature.default_value
