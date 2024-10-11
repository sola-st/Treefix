# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Get the embedding results.

    Returns a nested structure of `tf.Tensor` objects, matching the structure of
    the `feature_config` argument to the `TPUEmbedding` class. The output shape
    of the tensors is `(*output_shape, dim)`, `dim` is the dimension of the
    corresponding `TableConfig`. For output_shape, there are three places where
    it can be set.
      1. FeatureConfig provided in the __init__ function.
      2. Per_replica_output_shapes by directly calling the build method
           after initializing the tpu embedding class.
      3. Auto detected from the shapes of the input feature.
    The priority of these places is the exact same order.

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
      name: A name for the underlying op.

    Returns:
      A nested structure of tensors, with the same structure as `feature_config`
    passed to this instance of the `TPUEmbedding` object.

    Raises:
      RuntimeError: If called when object wasn't created under a `TPUStrategy`
        or if not built (either by manually calling build or calling enqueue).
    """
if not self._using_tpu:
    raise RuntimeError("dequeue is not valid when TPUEmbedding object is not "
                       "created under a TPUStrategy.")

if not self._built:
    raise RuntimeError("dequeue called on unbuilt TPUEmbedding object. "
                       "Please either call enqueue first or manually call "
                       "the build method.")

# The activations returned by this op are per feature.
activations = tpu_ops.recv_tpu_embedding_activations(
    num_outputs=len(self._config_proto.feature_descriptor),
    config=self._config_proto.SerializeToString())

# Apply the name tag to the op.
if name is not None:
    _add_key_attr(activations[0].op, name)

# Pack the list back into the same nested structure as the features.
exit(nest.pack_sequence_as(self._feature_config, activations))
