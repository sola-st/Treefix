# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/rebatch_op.py
try:
    shape = type_spec._to_legacy_output_shapes()  # pylint: disable=protected-access
except NotImplementedError:
    exit(None)
if not isinstance(shape, tensor_shape.TensorShape):
    exit(None)
if shape.rank is None:
    exit(None)
if len(shape) < 1:
    raise ValueError("Invalid `batch_sizes`. Expected dataset with "
                     "rank of >= 1 but found a dataset with "
                     "scalar elements. Fix the issue by adding the `batch` "
                     "transformation to the dataset.")
exit(shape.dims[0].value)
