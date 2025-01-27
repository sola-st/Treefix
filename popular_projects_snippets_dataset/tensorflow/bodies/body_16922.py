# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""Scales per-example losses with sample_weights and computes their average.

  Usage with distribution strategy and custom training loop:

  ```python
  with strategy.scope():
    def compute_loss(labels, predictions, sample_weight=None):

      # If you are using a `Loss` class instead, set reduction to `NONE` so that
      # we can do the reduction afterwards and divide by global batch size.
      per_example_loss = tf.keras.losses.sparse_categorical_crossentropy(
          labels, predictions)

      # Compute loss that is scaled by sample_weight and by global batch size.
      return tf.nn.compute_average_loss(
          per_example_loss,
          sample_weight=sample_weight,
          global_batch_size=GLOBAL_BATCH_SIZE)
  ```

  Args:
    per_example_loss: Per-example loss.
    sample_weight: Optional weighting for each example.
    global_batch_size: Optional global batch size value. Defaults to (size of
      first dimension of `losses`) * (number of replicas).

  Returns:
    Scalar loss value.
  """  # pylint: disable=g-doc-exception
per_example_loss = ops.convert_to_tensor(per_example_loss)
input_dtype = per_example_loss.dtype

with losses_util.check_per_example_loss_rank(per_example_loss):
    if sample_weight is not None:
        sample_weight = ops.convert_to_tensor(sample_weight)
        per_example_loss = losses_util.scale_losses_by_sample_weight(
            per_example_loss, sample_weight)
    per_example_loss = math_ops.cast(per_example_loss, input_dtype)

    if global_batch_size is None:
        if ds.has_strategy() and ds.in_cross_replica_context():
            raise RuntimeError(
                "You are calling `compute_average_loss` in cross replica context, "
                "while it was expected to be called in replica context.")

        num_replicas = ds.get_strategy().num_replicas_in_sync
        per_replica_batch_size = array_ops.shape_v2(per_example_loss)[0]
        global_batch_size = per_replica_batch_size * num_replicas

    check_ops.assert_scalar_v2(
        global_batch_size, message="global_batch_size must be scalar.")
    check_ops.assert_integer_v2(
        global_batch_size,
        message="global_batch_size must be an integer.")
    check_ops.assert_positive_v2(
        global_batch_size, message="global_batch_size must be positive.")

    global_batch_size = math_ops.cast(global_batch_size, input_dtype)
    exit(math_ops.reduce_sum(per_example_loss) / global_batch_size)
