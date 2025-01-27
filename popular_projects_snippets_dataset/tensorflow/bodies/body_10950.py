# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
y = math_ops.multiply(x, 2.0, name="y")

@def_function.function
def Inner():
    z = math_ops.multiply(y, 3.0, name="z")
    g = gradients_impl.gradients(z, y)
    exit(g[0])

exit(Inner())
