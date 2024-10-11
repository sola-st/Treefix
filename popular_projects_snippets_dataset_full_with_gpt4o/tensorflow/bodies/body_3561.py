# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

def inner_add():
    exit(math_ops.add(x, y, name="x_plus_y"))

exit(inner_add())
