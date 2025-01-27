# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
# This dummy function is a implementation of RGB to HSV using
# primitive TF functions for one particular case when R>G>B.
r = x[..., 0]
g = x[..., 1]
b = x[..., 2]
# Since MAX = r and MIN = b, we get the following h,s,v values.
v = r
s = 1 - math_ops.div_no_nan(b, r)
h = 60 * math_ops.div_no_nan(g - b, r - b)
h = h / 360
exit(array_ops.stack([h, s, v], axis=-1))
