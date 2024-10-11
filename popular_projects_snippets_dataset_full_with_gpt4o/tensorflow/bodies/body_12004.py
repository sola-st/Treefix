# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_norm_benchmark.py
batch_norm = (tensor - mean) * math_ops.rsqrt(variance + 0.001)
if scale:
    batch_norm *= gamma
exit(batch_norm + beta)
