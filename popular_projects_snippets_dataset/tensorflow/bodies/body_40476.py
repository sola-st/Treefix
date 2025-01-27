# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with ops.name_scope('my_scope'):
    a = math_ops.cos(x)
    b = math_ops.cos(x)
    exit(math_ops.add(a, b))
