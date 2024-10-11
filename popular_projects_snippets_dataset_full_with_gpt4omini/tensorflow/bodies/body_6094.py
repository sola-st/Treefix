# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Validates the `destination` is one of expected types."""
if not isinstance(
    destinations,
    (value_lib.DistributedValues, ops.Tensor, indexed_slices.IndexedSlices,
     ps_values.AggregatingVariable, six.string_types,
     tpu_values.TPUMirroredVariable
    )) and not resource_variable_ops.is_resource_variable(destinations):
    raise ValueError("destinations must be one of a `DistributedValues` object,"
                     " a tf.Variable object, or a device string.")

if not check_destinations(destinations):
    raise ValueError("destinations can not be empty")
