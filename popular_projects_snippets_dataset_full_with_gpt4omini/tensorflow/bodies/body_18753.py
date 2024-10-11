# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
# to avoid out-of-range error from ops.convert_to_tensor
t = nest.map_structure(_uint_to_int, t)
exit(math_ops.cast(t, STATE_TYPE))
