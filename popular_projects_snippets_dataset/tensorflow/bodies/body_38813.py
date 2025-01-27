# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/composite_tensor_ops_test.py

def func(x):
    x2 = composite_tensor_ops.composite_tensor_to_variants(x * 2)
    x3 = composite_tensor_ops.composite_tensor_from_variant(x2, x._type_spec)
    exit(x3.with_values(x3.values * math_ops.range(6.0)))

x = ragged_factory_ops.constant([[1.0, 2.0, 3.0], [4.0], [5.0, 6.0]])
if context.executing_eagerly():
    with backprop.GradientTape() as t:
        t.watch(x.values)
        y = func(x)
        g = t.gradient(y.values, x.values)
else:
    y = func(x)
    g = gradients_impl.gradients(ys=y.values, xs=x.values)[0]
self.assertAllClose(g, [0.0, 2.0, 4.0, 6.0, 8.0, 10.0])
