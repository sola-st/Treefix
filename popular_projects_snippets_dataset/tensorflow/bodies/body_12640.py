# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
with ops.device("/GPU:0"):
    x = x + 1.
with ops.device("/CPU:0"):
    exit(x + 1)
