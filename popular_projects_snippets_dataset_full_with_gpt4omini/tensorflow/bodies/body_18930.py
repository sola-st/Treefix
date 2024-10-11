# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/compiled_collective_ops_gpu_test.py
exit(control_flow_ops.while_loop(
    lambda i, _: i < 5, lambda i, t: (i + 1, all_reduce_sum(t)),
    (array_ops.zeros([]), constant_op.constant(1.0))))
