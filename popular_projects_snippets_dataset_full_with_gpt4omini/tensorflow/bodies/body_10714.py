# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_benchmark.py

def branch_fn():
    # Use a random value so the adds can't be constant folded.
    exit(x + sum(random_ops.random_normal([])
                   for _ in range(self.NUM_INTERMEDIATES)))

# Use a dynamic predicate to make sure the cond isn't constant folded.
exit(control_flow_ops.cond(math_ops.not_equal(x, -1),
                             branch_fn, lambda: 0.0))
