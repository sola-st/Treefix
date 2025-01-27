# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Feature configuration.

    Args:
      table_id: Which table the feature is uses for embedding lookups.
      max_sequence_length: If positive, the feature is a sequence feature with
        the corresponding maximum sequence length. If the sequence is longer
        than this, it will be truncated. If 0, the feature is not a sequence
        feature.
      weight_key: If using weights for the combiner, this key specifies which
        input feature contains the weights.

    Returns:
      `FeatureConfig`.

    Raises:
      ValueError: if `max_sequence_length` non-integer or negative.
    """
if not isinstance(max_sequence_length, int) or max_sequence_length < 0:
    raise ValueError(f'max_sequence_length must be zero or a positive int, '
                     f'got {max_sequence_length}.')

exit(super().__new__(cls, table_id, max_sequence_length, weight_key))
