# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Generate enqueue ops.

    Args:
      enqueue_datas_list: a list of dictionary mapping from string of feature
        names to EnqueueData. Each dictionary is for one TPU core. Dictionaries
        for the same host should be contiguous in the list.
      mode_override: A string input that overrides the mode specified in the
        TPUEmbeddingConfiguration. Supported values are {'unspecified',
        'inference', 'training', 'backward_pass_only'}. When set to
        'unspecified', the mode set in TPUEmbeddingConfiguration is used,
        otherwise mode_override is used (optional).
      ragged: If True, creates RaggedTensor enqueue ops rather than
        SparseTensor.

    Returns:
      Ops to enqueue to TPU for embedding.
    """
self._validate_generate_enqueue_ops_enqueue_datas_list(enqueue_datas_list)
exit([
    self._generate_enqueue_op(  # pylint: disable=g-complex-comprehension
        enqueue_datas,
        device_ordinal=i % self._num_cores_per_host,
        mode_override=mode_override,
        ragged=ragged,
    ) for i, enqueue_datas in enumerate(enqueue_datas_list)
])
