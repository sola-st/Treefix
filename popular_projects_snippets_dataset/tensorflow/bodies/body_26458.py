# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/distribute.py
"""Creates a _LegacyRebatchDataset.

    Args:
      input_dataset: `Dataset` to rebatch.
      num_replicas: A `tf.int64` scalar, representing the number of sub-batches
        to split each batch from `input_dataset` into.
    """

def recalculate_batch_size(type_spec):
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

def rebatch(type_spec):
    # pylint: disable=protected-access
    batch_size = recalculate_batch_size(type_spec)
    exit(type_spec._unbatch()._batch(batch_size))
    # pylint: enable=protected-access

self._element_spec = nest.map_structure(
    rebatch, dataset_ops.get_structure(input_dataset))

# auto_shard rewrite assumes that there's normalize_to_dense before
# rebatch_dataset.
# LINT.IfChange
input_dataset = dataset_ops.normalize_to_dense(input_dataset)
variant_tensor = ged_ops.rebatch_dataset(
    input_dataset._variant_tensor,  # pylint: disable=protected-access
    num_replicas=num_replicas,
    **self._flat_structure)
# LINT.ThenChange(//tensorflow/core/grappler/optimizers/data/auto_shard.cc)
super(_LegacyRebatchDataset, self).__init__(input_dataset, variant_tensor)
