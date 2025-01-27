# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
for val in inputs:
    v.assign(math_ops.matmul(v, val))
