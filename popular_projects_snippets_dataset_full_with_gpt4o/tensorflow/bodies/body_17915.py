# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with self.assertRaisesRegex(ValueError, "positive integer"):
    pfor_control_flow_ops.pfor(lambda i: 1, 8, parallel_iterations=0)
with self.assertRaisesRegex(TypeError, "positive integer"):
    pfor_control_flow_ops.for_loop(
        lambda i: 1, dtypes.int32, 8, parallel_iterations=0)
