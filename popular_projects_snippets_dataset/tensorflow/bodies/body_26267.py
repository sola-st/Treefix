# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
# Add tiny to initial_probs to avoid divide by zero.
denom = (initial_probs + np.finfo(initial_probs.dtype.as_numpy_dtype).tiny)
exit(target_probs / denom)
