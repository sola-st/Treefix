# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

@def_function.function
def inner_add():
    exit(math_ops.add(y, z, name="x_plus_y"))

exit(math_ops.add(x, inner_add(), name="x_plus_y"))
