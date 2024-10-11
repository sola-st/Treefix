# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
pointwise = math_ops.sin(x) * math_ops.tan(x)
exit(math_ops.reduce_prod(
    pointwise + math_ops.reduce_sum(pointwise), axis=1))
