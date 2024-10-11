# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
# Padding with zeros on the left. The zeros will be the counter.
exit([0] * (_get_state_size(alg) - 1) + [key])
