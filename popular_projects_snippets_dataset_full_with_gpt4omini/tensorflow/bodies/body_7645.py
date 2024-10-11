# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
input0, input1 = inputs
exit((array_ops.size(input0), math_ops.reduce_sum(input1)))
