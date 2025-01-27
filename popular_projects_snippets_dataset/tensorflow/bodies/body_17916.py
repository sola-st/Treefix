# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with self.assertRaisesRegex(ValueError, "Use `for_loop` instead"):
    pfor_control_flow_ops.pfor(lambda i: 1, 8, parallel_iterations=1)
