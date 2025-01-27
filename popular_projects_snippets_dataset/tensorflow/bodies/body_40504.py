# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = array_ops.zeros([3])
with backprop.GradientTape(persistent=True) as tape:
    tape.watch(x)
    result = def_function.function(
        functools.partial(functional_ops.foldl_v2, lambda a, b: a + b))(
            x)
self.assertAllClose([1., 1., 1.],
                    tape.jacobian(result, x, experimental_use_pfor=True))
self.assertAllClose([1., 1., 1.],
                    tape.jacobian(result, x, experimental_use_pfor=False))

# Non-persistent tapes take a different function gradient path, but also
# work with pfor=True.
x = array_ops.zeros([3])
with backprop.GradientTape() as tape:
    tape.watch(x)
    result = def_function.function(
        functools.partial(functional_ops.foldl_v2, lambda a, b: a + b))(
            x)
self.assertAllClose([1., 1., 1.],
                    tape.jacobian(result, x, experimental_use_pfor=True))
