# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
"""A placeholder op for feeding per-sample gradients to the embedding layer.

  Args:
    inputs: A TensorList of gradients with which to update embedding tables.
      This argument has the same length and shapes as the return value of
      RecvTPUEmbeddingActivations, but contains gradients of the model's loss
      with respect to the embedding activations. The embedding tables are
      updated from these gradients via the optimizers specified in the TPU
      embedding configuration given to tpu.initialize_system.
    config: Serialized TPUEmbeddingConfiguration proto.
    learning_rates: A TensorList of float32 scalars, one for each dynamic
        learning rate tag: see the comments in
          //third_party/tensorflow/core/protobuf/tpu/
          optimization_parameters.proto. Multiple tables can share the same
          dynamic learning rate tag as specified in the configuration. If the
          learning rates for all tables are constant, this list should be empty.
    name: A name for the operation (optional).

  Returns:
    A SendTPUEmbeddingGradients operation.
  """
if learning_rates is None:
    learning_rates = []
exit(gen_tpu_ops.send_tpu_embedding_gradients(
    inputs=inputs, learning_rates=learning_rates, config=config, name=name))
