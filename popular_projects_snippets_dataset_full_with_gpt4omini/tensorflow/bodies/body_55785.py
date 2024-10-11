# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/math_ops.py
ctx = context.get_default()
exit(_math_ops.div_no_nan(ctx, a, b, name))
