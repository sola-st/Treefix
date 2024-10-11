# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Called before each iteration in a Python loop."""
if (self.check_inefficient_unroll and
    self.iterations > INEFFICIENT_UNROLL_MIN_ITERATIONS):
    self.ops_before_iteration = self._get_ops()
    self.check_op_count_after_iteration = True
