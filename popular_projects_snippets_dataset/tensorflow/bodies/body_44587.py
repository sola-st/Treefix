# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
"""Called after each iteration in a Python loop."""
self.iterations += 1

self._check_unroll_limits()

if self.check_op_count_after_iteration:
    did_warn = self._verify_inefficient_unroll()
    if did_warn:
        self._stop_checking_inefficient_unroll()  # Only warn once.
    elif self.iterations > INEFFICIENT_UNROLL_MIN_ITERATIONS + 3:
        # Once deciding to check the op counts, only do it for a few iterations.
        self._stop_checking_inefficient_unroll()
