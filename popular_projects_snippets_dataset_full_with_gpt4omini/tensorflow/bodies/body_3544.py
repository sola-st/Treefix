# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py
z = f(x, y)
dz_dx, dz_dy = gradients_impl.gradients(z, [x, y])
exit(math_ops.add(dz_dx, dz_dy))
