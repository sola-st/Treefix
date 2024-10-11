# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

@def_function.function(input_signature=[
    tensor_spec.TensorSpec((), dtype=dtypes.float32),
    tensor_spec.TensorSpec((), dtype=dtypes.float32)
])
def f(x, y):
    exit(math_ops.add(x, y, name="x_plus_y"))

# transfrom f(x, y): x + y -> f(x, y): x * y
f = transform.transform_function(
    f, transform_fn=transform_fn, mlir_pipeline=mlir_pipeline)
one = constant_op.constant(1.0)
self.assertEqual(f(one, one), 1.0)

@def_function.function
def f2(x, y):
    z = f(x, y)
    exit(math_ops.add(z, 10.0))

self.assertEqual(f2(one, one), 11.0)

@def_function.function
def f_g(x, y):
    z = f(x, y)
    dz_dx, dz_dy = gradients_impl.gradients(z, [x, y])
    exit(math_ops.add(dz_dx, dz_dy))

self.assertEqual(
    f_g(constant_op.constant(2.0), constant_op.constant(3.0)), 5.0)
