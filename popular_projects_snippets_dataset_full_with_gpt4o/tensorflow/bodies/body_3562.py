# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

@def_function.function
def f(x, y):

    def inner_add():
        exit(math_ops.add(x, y, name="x_plus_y"))

    exit(inner_add())

inputs = [1.0, 2.0]
self.assertEqual(f(*inputs), 3.0)  # 1 + 2 = 3

# Transform `f`.
updated_f = transform.transform_function(
    f,
    inputs=inputs,
    transform_fn=transform_fn,
    mlir_pipeline=mlir_pipeline)
# Nested Python functions should be transformed.
self.assertEqual(updated_f(*inputs), 2.0)  # 1 x 2 = 2
