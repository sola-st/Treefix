# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Runs validation checks on input and target data passed by the user.

    This is called when using tf.distribute.Strategy to train, evaluate or serve
    the model.

    Args:
      x: Input data. A numpy array or `tf.data` dataset.
      y: Target data. A numpy array or None if x is a `tf.data` dataset.
      sample_weight: An optional sample-weight array passed by the user to
        weight the importance of each sample in `x`.
      class_weight: An optional class-weight array by the user to
        weight the importance of samples in `x` based on the class they belong
        to, as conveyed by `y`.
      batch_size: Integer batch size. If provided, it is used to run additional
        validation checks on stateful models.
      validation_split: Float between 0 and 1.
        Fraction of the training data to be used as validation data.
      shuffle: Boolean whether to shuffle the training data before each epoch.
      epochs: Integer epochs. If > 1, repeat the numpy training data epochs
        times when converting to training dataset.
      allow_partial_batch: Boolean whether to enforce that all batches have the
        same size.

    Returns:
      Dataset instance.

    Raises:
      ValueError: In case of invalid user-provided data.
      RuntimeError: If the model was never compiled.
    """
if class_weight:
    raise NotImplementedError('`class_weight` is currently not supported '
                              'when using tf.distribute.Strategy.')

if (sample_weight is not None and sample_weight.all() and
    backend.is_tpu_strategy(self._distribution_strategy)):
    raise NotImplementedError('`sample_weight` is currently not supported '
                              'when using TPUStrategy.')

# Validates `steps` and `shuffle` arguments right at the beginning
# since we use it to construct the dataset object.
# TODO(anjalisridhar): Remove this check once we refactor the
# _standardize_user_data code path. This check is already present elsewhere
# in the codebase.
if isinstance(x, dataset_ops.DatasetV2):
    if shuffle:
        training_utils_v1.verify_dataset_shuffled(x)

strategy = self._distribution_strategy
with strategy.scope():
    # We should be sure to call get_session() inside the strategy.scope()
    # so the strategy can affect the session options.
    if ops.executing_eagerly_outside_functions():
        session = None
    else:
        session = backend.get_session()

    first_x_value = nest.flatten(x)[0]
    if isinstance(first_x_value, np.ndarray):
        x = training_utils.list_to_tuple(x)
        if y is not None:
            y = training_utils.list_to_tuple(y)
            if sample_weight is not None:
                sample_weight = training_utils.list_to_tuple(sample_weight)
                in_tuple = (x, y, sample_weight)
            else:
                in_tuple = (x, y)
        else:
            in_tuple = x

        ds = strategy.extended.experimental_make_numpy_dataset(in_tuple,
                                                               session=session)
        if shuffle:
            # We want a buffer size that is larger than the batch size provided by
            # the user and provides sufficient randomness. Note that larger
            # numbers introduce more memory usage based on the size of each
            # sample.
            ds = ds.shuffle(max(1024, batch_size * 8))
        if epochs > 1:
            ds = ds.repeat(epochs)

        # We need to use the drop_remainder argument to get a known static
        # input shape which is required for TPUs.
        drop_remainder = (not allow_partial_batch and
                          strategy.extended.experimental_require_static_shapes)

        # TODO(b/131720208): We still drop remainder here if number of examples
        # is divisible by batch size, as sometimes dynamic padder will time out
        # with keras.metrics.CategoricalAccuracy() metric.
        if backend.is_tpu_strategy(strategy) and not drop_remainder:
            dataset_size = first_x_value.shape[0]
            if dataset_size % batch_size == 0:
                drop_remainder = True

        x = ds.batch(batch_size, drop_remainder=drop_remainder)
    else:
        assert isinstance(x, dataset_ops.DatasetV2)
        training_utils_v1.validate_dataset_input(x, y, sample_weight,
                                                 validation_split)
exit(x)
