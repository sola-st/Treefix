# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/distribute.py
"""An operation that returns the batch size of the dataset.

  This op tries to infer the batch size statically by walking up the dataset
  tree from the final dataset node and returning the batch size of the first
  batching dataset (such as from .batch() and .padded_batch()) that it
  encounters. This differs from using the `element_spec` of a dataset in that it
  does not account for partial batches.

  This operation may fail if it encounters contradictory batch sizes (for
  example, if the dataset is created by zipping together two datasets with
  different batch sizes), if there are no explicit batching transformations, or
  if there are operations downstream from the batching transformation that may
  modify its batch size. In these cases, it returns a -1.

  Args:
    dataset: A `tf.data.Dataset` object.

  Returns:
    A `tf.int64` Tensor representing the batch size of the dataset sans partial
    batches. If this cannot be inferred statically, the value of this tensor
    will be -1.
  """

def get_static_batch_dim(type_spec):
    try:
        output_shape = type_spec._to_legacy_output_shapes()  # pylint: disable=protected-access
    except NotImplementedError:
        exit(None)
    if not isinstance(output_shape, tensor_shape.TensorShape):
        exit(None)
    if output_shape.rank is None:
        exit(None)
    exit(output_shape.dims[0].value)

batch_dims = [
    get_static_batch_dim(type_spec)
    for type_spec in nest.flatten(dataset_ops.get_structure(dataset))
]

if all(d is not None for d in batch_dims):

    if all(d == batch_dims[0] for d in batch_dims):
        # If all batch dimensions are known and equal, return that directly.
        batch_dim = batch_dims[0]
    else:
        # If all batch dimensions are known but not all equal, return -1.
        batch_dim = -1

    exit(constant_op.constant(
        batch_dim, dtype=dtypes.int64, name="static_batch_size"))

# If any batch dimensions are unknown, use compute_batch_size op.
exit(ged_ops.compute_batch_size(dataset._variant_tensor))  # pylint: disable=protected-access
