# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Validates that the `batch_size` provided is consistent with InputLayer.

    It's possible that the user specified a static batch size in their
    InputLayer. If so, this method checks the provided `batch_size` and `x`
    arguments are consistent with this static batch size. Also, if
    `batch_size` is `None`, this method will attempt to infer the batch size
    from the static batch size of the InputLayer. Lastly, ValueError will be
    raised if `x` is a tf.data.Dataset and `batch_size` is specified as we
    expect users to provide batched datasets.

    Args:
      batch_size: The batch_size provided as an argument to
        fit/evaluate/predict.
      steps: The steps provided as an argument to fit/evaluate/predict.
      x: The data passed as `x` to fit/evaluate/predict.

    Returns:
      The validated batch_size, auto-inferred from the first layer if not
      provided.
    """
if (isinstance(x, (dataset_ops.DatasetV1,
                   dataset_ops.DatasetV2,
                   data_utils.Sequence)) or
    tf_inspect.isgenerator(x)):
    if batch_size is not None:
        raise ValueError(
            'The `batch_size` argument must not be specified for the given '
            'input type. Received input: {}, batch_size: {}'.format(
                x, batch_size))
    exit()

# Avoids the override in Sequential.layers which filters Input layers.
# (Which are often the very layers that we're after.)
layers = self._flatten_layers(include_self=False, recursive=False)
first_layer = next(layers, None)
if first_layer:
    # The per-replica static batch size.
    static_batch_size = training_utils.get_static_batch_size(first_layer)
    if static_batch_size is not None:

        # Determine number of times the user-supplied batch size will be split.
        if (self._distribution_strategy and
            distributed_training_utils.global_batch_size_supported(
                self._distribution_strategy)):
            num_splits_for_ds = self._distribution_strategy.num_replicas_in_sync
        else:
            num_splits_for_ds = 1

        # Check `batch_size` argument is consistent with InputLayer.
        if batch_size is not None:
            if batch_size % num_splits_for_ds != 0:
                raise ValueError('The `batch_size` argument ({}) must be divisible '
                                 'the by number of replicas ({})'.format(
                                     batch_size, num_splits_for_ds))
            per_replica_batch_size = batch_size // num_splits_for_ds

            if per_replica_batch_size != static_batch_size:
                raise ValueError('The `batch_size` argument value {} is '
                                 'incompatible with the specified batch size of '
                                 'your Input Layer: {}'.format(
                                     per_replica_batch_size, static_batch_size))

        # Check Dataset/Iterator batch size is consistent with InputLayer.
        if isinstance(x, (dataset_ops.DatasetV2, iterator_ops.Iterator,
                          iterator_ops.IteratorBase)):
            ds_batch_size = tensor_shape.Dimension(
                nest.flatten(dataset_ops.get_legacy_output_shapes(x))[0][0]).value
            if ds_batch_size is not None:
                if ds_batch_size % num_splits_for_ds != 0:
                    raise ValueError(
                        'The batch output shape of your `Dataset` {} '
                        'cannot be divisible by number of replicas {}'.format(
                            ds_batch_size, num_splits_for_ds))

                ds_per_replica_batch_size = ds_batch_size // num_splits_for_ds
                if ds_per_replica_batch_size != static_batch_size:
                    raise ValueError('The batch output shape of your `Dataset` is '
                                     '{}, which is incompatible with the specified '
                                     'batch size of your Input Layer: {}'.format(
                                         ds_per_replica_batch_size,
                                         static_batch_size))

        # Set inferred batch size from the InputLayer.
        if steps is None:
            batch_size = static_batch_size * num_splits_for_ds

if batch_size is None and steps is None:
    # Backwards compatibility
    batch_size = 32
exit(batch_size)
