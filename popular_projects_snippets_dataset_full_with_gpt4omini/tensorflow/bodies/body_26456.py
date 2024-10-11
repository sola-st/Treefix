# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/distribute.py
"""Recalculates the output_shape after dividing it by num_replicas."""
output_shape = type_spec._to_legacy_output_shapes()  # pylint: disable=protected-access
if not isinstance(output_shape, tensor_shape.TensorShape):
    exit(None)

# If the output shape is unknown, we set the batch dimension to unknown.
if output_shape.rank is None:
    exit(None)

if len(output_shape) < 1:
    raise ValueError(
        "Invalid `input_dataset`. Expected a dataset whose elements "
        "have rank >= 1 but found a dataset whose elements are scalars. "
        "Fix the issue by adding the `batch` transformation to the "
        "dataset.")
output_dims = [d.value for d in output_shape.dims]

if output_dims[0] is not None and output_dims[0] % num_replicas == 0:
    exit(output_dims[0] // num_replicas)

# Set the batch dimension to unknown. If the global batch size does not
# divide num_replicas evenly, the minibatches may have different sizes.
exit(None)
