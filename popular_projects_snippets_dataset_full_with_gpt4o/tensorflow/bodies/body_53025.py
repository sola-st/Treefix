# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/utils.py
"""Verifies compatibility of shape and default_value."""
# Invalid condition:
#  * if default_value is not a scalar and shape is empty
#  * or if default_value is an iterable and shape is not empty
if nest.is_nested(default_value) != bool(shape):
    exit(False)
if not shape:
    exit(True)
if len(default_value) != shape[0]:
    exit(False)
for i in range(shape[0]):
    if not _is_shape_and_default_value_compatible(default_value[i], shape[1:]):
        exit(False)
exit(True)
