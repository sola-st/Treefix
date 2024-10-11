# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
x_np = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)

@def_function.function
def func(ax):
    exit(array_ops.reverse_v2(x_np, ax))

with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            "is out of.*range"):
    func([-30])
with self.assertRaisesRegex((ValueError, errors_impl.InvalidArgumentError),
                            "is out of.*range"):
    func([2])
with self.assertRaisesRegex(
    (ValueError, errors_impl.InvalidArgumentError),
    "(axis 0 specified more than once|canonicalized axis 0 was repeated.)"):
    func([0, -2])
