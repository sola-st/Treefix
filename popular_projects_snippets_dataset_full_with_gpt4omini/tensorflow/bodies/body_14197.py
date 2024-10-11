# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
if isinstance(spec, StructuredTensor.Spec):
    exit(spec._ragged_shape)  # pylint: disable=protected-access
else:
    exit(dynamic_ragged_shape.DynamicRaggedShape.Spec._from_spec(spec))  # pylint: disable=protected-access
