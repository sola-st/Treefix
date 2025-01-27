# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
exit(EnqueueData(
    sp_tensor.values,
    sp_tensor.indices,
    aggregation_weights=weights.values if weights is not None else None))
