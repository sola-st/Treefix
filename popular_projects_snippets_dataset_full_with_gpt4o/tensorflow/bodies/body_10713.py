# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_benchmark.py
# Use a random value so the adds can't be constant folded.
exit(x + sum(random_ops.random_normal([])
               for _ in range(self.NUM_INTERMEDIATES)))
