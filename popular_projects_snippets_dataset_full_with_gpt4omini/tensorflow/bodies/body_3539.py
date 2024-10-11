# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py
r = math_ops.add(x, y, name="x_plus_y")
if add_2:
    exit(r + 2)
else:
    exit(r)
