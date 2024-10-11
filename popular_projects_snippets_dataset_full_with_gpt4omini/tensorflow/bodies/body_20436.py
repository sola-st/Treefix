# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
"""Checks for invalid embedding_lookup_device configurations."""
if (tpu.under_tpu_inference_context() and
    embedding_lookup_device == EmbeddingDevice.TPU_EMBEDDING_CORE):
    raise ValueError(
        'Using embedding_lookup_device=tpu_embedding_core during inference '
        'is not supported.')
if embedding_lookup_device == EmbeddingDevice.CPU:
    if not tpu.under_tpu_inference_context():
        raise ValueError(
            'Using TPUEmbeddingColumn with embedding_lookup_device="cpu" '
            'during training is not supported.')
