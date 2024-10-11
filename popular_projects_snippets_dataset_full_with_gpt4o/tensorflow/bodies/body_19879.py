# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Applies the gradient update to the embedding tables.

    If a gradient of `None` is passed in any position of the nested structure,
    then an gradient update with a zero gradient is applied for that feature.
    For optimizers like SGD or Adagrad, this is the same as applying no update
    at all. For lazy Adam and other sparsely applied optimizers with decay,
    ensure you understand the effect of applying a zero gradient.

    ```python
    strategy = tf.distribute.TPUStrategy(...)
    with strategy.scope():
      embedding = tf.tpu.experimental.embedding.TPUEmbedding(...)

    distributed_dataset = (
        strategy.distribute_datasets_from_function(
            dataset_fn=...,
            options=tf.distribute.InputOptions(
                experimental_fetch_to_device=False))
    dataset_iterator = iter(distributed_dataset)

    @tf.function
    def training_step():
      def tpu_step(tpu_features):
        with tf.GradientTape() as tape:
          activations = embedding.dequeue()
          tape.watch(activations)

          loss = ... #  some computation involving activations

        embedding_gradients = tape.gradient(loss, activations)
        embedding.apply_gradients(embedding_gradients)

      embedding_features, tpu_features = next(dataset_iterator)
      embedding.enqueue(embedding_features, training=True)
      strategy.run(tpu_step, args=(tpu_features, ))

    training_step()
    ```

    Args:
      gradients: A nested structure of gradients, with structure matching the
        `feature_config` passed to this object.
      name: A name for the underlying op.

    Raises:
      RuntimeError: If called when object wasn't created under a `TPUStrategy`
        or if not built (either by manually calling build or calling enqueue).
      ValueError: If a non-`tf.Tensor` non-`None` gradient is passed in, or a
        `tf.Tensor` of the incorrect shape is passed in. Also if
        the size of any sequence in `gradients` does not match corresponding
        sequence in `feature_config`.
      TypeError: If the type of any sequence in `gradients` does not match
        corresponding sequence in `feature_config`.
    """
if not self._using_tpu:
    raise RuntimeError("apply_gradients is not valid when TPUEmbedding "
                       "object is not created under a TPUStrategy.")

if not self._built:
    raise RuntimeError("apply_gradients called on unbuilt TPUEmbedding "
                       "object. Please either call enqueue first or manually "
                       "call the build method.")

nest.assert_same_structure(self._feature_config, gradients)
updated_gradients = []
for (path, gradient), feature, output_shape in zip(
    nest.flatten_with_joined_string_paths(gradients),
    nest.flatten(self._feature_config), self._output_shapes):
    full_output_shape = list(output_shape) + [feature.table.dim]
    if gradient is not None and not isinstance(gradient, ops.Tensor):
        raise ValueError(
            f"found non-tensor type: {type(gradient)} at path {path}.")
    if gradient is not None:
        if gradient.shape != full_output_shape:
            raise ValueError("Found gradient of shape {} at path {}. Expected "
                             "shape {}.".format(gradient.shape, path,
                                                full_output_shape))
    else:
        # No gradient for this feature, since we must give a gradient for all
        # features, pass in a zero tensor here. Note that this is not correct
        # for all optimizers.
        logging.warning(
            "No gradient passed for feature %s, sending zero "
            "gradient. This may not be correct behavior for certain "
            "optimizers like Adam.", path)
        gradient = array_ops.zeros(full_output_shape, dtype=dtypes.float32)
    # Some gradients can be passed with op which shape is not correctly set.
    # This ensures that the shape of the gradient is correctly set.
    updated_gradients.append(
        array_ops.reshape(gradient, shape=gradient.shape))
op = tpu_ops.send_tpu_embedding_gradients(
    inputs=updated_gradients,
    learning_rates=[
        math_ops.cast(fn(), dtype=dtypes.float32)
        for fn in self._dynamic_learning_rates
    ],
    config=self._config_proto.SerializeToString())

# Apply the name tag to the op.
if name is not None:
    _add_key_attr(op, name)
