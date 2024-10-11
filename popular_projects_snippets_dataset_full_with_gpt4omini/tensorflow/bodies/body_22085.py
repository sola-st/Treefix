# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
exit(state_ops.assign_sub(v, (v - value) * decay, name=scope))
