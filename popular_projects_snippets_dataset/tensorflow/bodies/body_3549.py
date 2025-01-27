# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

@def_function.function
def f(x, y):
    exit(math_ops.add(x, y, name="x_plus_y"))

one = constant_op.constant(1.0)

# transfrom f(x, y): x + y -> f(x, y): x * y
g = transform.transform_function(
    f,
    inputs=None,
    kw_inputs={"x": one, "y": one},
    transform_fn=add_to_multiply,
    mlir_pipeline="test-pass")

self.assertEqual(g(one, one), 1.0)
self.assertEqual(g(one, y=one), 1.0)
self.assertEqual(g(x=one, y=one), 1.0)
