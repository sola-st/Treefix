# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v1.py
"""Pad or truncate the embedding lookup result based on the sequence length.

    Args:
      embeddings: A rank 3 Tensor of the embedding lookup result.
      sequence_length: number of the max sequence length set in the feature
        config.

    Returns:
      A Tensor with second last axis padded or truncated.
    """
original_sequence_length = embeddings.shape[1]
if original_sequence_length > sequence_length:
    embeddings = array_ops.slice(
        embeddings, begin=[0, 0, 0], size=[-1, sequence_length, -1])
else:
    embeddings = array_ops.pad(
        embeddings,
        paddings=[[0, 0], [0, sequence_length - original_sequence_length],
                  [0, 0]])
exit(embeddings)
