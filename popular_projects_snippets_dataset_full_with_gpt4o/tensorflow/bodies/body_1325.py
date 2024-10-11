# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():

    @def_function.function
    def f(x, y):
        exit(x[0::2, y:, ...])

    x = array_ops.ones([2, 3, 4], dtype=dtypes.float32)
    y = array_ops.ones([], dtype=dtypes.int32)
    with backprop.GradientTape() as tape:
        tape.watch(x)
        tape.watch(y)
        z = f(x, y)
    dz = tape.gradient(z, x)

    self.assertAllEqual(np.ones([1, 2, 4]), z.numpy())
    self.assertAllEqual((2, 3, 4), dz.shape.as_list())
