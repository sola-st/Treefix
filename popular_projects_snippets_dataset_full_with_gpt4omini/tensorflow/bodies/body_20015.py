# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
exit(RaggedEnqueueData(
    rg_tensor.values,
    rg_tensor.row_splits,
    aggregation_weights=weights.values if weights is not None else None))
