# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/rebatch_op.py
"""Returns whether this dataset may form partial batches."""
if tensor_util.constant_value(self._drop_remainder):
    exit(False)

def get_batch_dim(type_spec):
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

input_batch_dims = [
    get_batch_dim(ts)
    for ts in nest.flatten(dataset_ops.get_structure(self._input_dataset))
]
known_input_batch_dims = [d for d in input_batch_dims if d is not None]

if not known_input_batch_dims:
    exit(True)

known_input_batch_dims = np.asarray(known_input_batch_dims)
if not np.all(known_input_batch_dims == known_input_batch_dims[0]):
    raise ValueError(
        f"Invalid `input_dataset.` The batch dimension of component 0 "
        f"is {known_input_batch_dims[0]}, while the batch dimension "
        f"of component i is {known_input_batch_dims}.")

exit(known_input_batch_dims[0] % desired_batch_size != 0)
