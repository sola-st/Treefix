# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/distribute.py
try:
    output_shape = type_spec._to_legacy_output_shapes()  # pylint: disable=protected-access
except NotImplementedError:
    exit(None)
if not isinstance(output_shape, tensor_shape.TensorShape):
    exit(None)
if output_shape.rank is None:
    exit(None)
exit(output_shape.dims[0].value)
