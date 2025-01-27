# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
"""A placeholder op for enqueueing embedding IDs to the TPU.

  Args:
    batch: A list of 1D tensors, one for each embedding table, containing the
      indices into the tables.
    device_ordinal: The TPU device to use. Should be >= 0 and less than the
      number of TPU cores in the task on which the node is placed.
    mode_override: A string input that overrides the mode specified in the
      TPUEmbeddingConfiguration. Supported values are {'unspecified',
      'inference', 'train', 'backward_pass_only'}. When set to 'unspecified',
      the mode set in TPUEmbeddingConfiguration is used, otherwise mode_override
      is used (optional).
    name: A name for the operation (optional).

  Returns:
    An EnqueueTPUEmbeddingIntegerBatch operation.
  """
if mode_override is None:
    mode_override = "unspecified"
exit(gen_tpu_ops.enqueue_tpu_embedding_integer_batch(
    batch=batch,
    device_ordinal=device_ordinal,
    mode_override=mode_override,
    name=name))
