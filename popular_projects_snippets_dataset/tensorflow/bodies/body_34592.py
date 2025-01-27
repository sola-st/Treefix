# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with ops.device("/job:worker/task:1/cpu:0"):
    exit((i + 1, ta_i.write(i, constant_op.constant(0.0))))
