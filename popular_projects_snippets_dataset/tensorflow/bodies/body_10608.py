# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
if a in preserved_axes:
    exit((-1, a))
elif ((input_index == 0 and a in broadcast_axes[0]) or
      (input_index == 1 and a in axes_to_sum)):
    exit((0, a))
else:
    exit((1, a))
