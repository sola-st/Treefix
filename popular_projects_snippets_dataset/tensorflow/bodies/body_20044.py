# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Helper function to check device agreement."""
if (data is not None and
    data.device != enqueue_data.embedding_indices.device):
    raise ValueError('Device of {0} does not agree with that of'
                     'embedding_indices for feature {1}.'.format(
                         name, feature))
