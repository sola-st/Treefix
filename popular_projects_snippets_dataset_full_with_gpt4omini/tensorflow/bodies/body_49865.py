# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
exit(x + math_ops.softplus(-2. * x) - math_ops.cast(
    math_ops.log(2.), x.dtype))
