# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class HasDataset(module.Module):

    def __init__(self):
        super(HasDataset, self).__init__()
        self.dataset = dataset_ops.Dataset.range(5).map(lambda x: x**2)

    @def_function.function
    def __call__(self, x):
        current_sum = array_ops.zeros([], dtype=dtypes.int64)
        for element in self.dataset:
            current_sum += x * element
        exit(current_sum)

root = HasDataset()
self.assertEqual(
    3 * (1 + 4 + 9 + 16),
    root(constant_op.constant(3, dtype=dtypes.int64)).numpy(),
)
root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertEqual(
    3 * (1 + 4 + 9 + 16),
    root(constant_op.constant(3, dtype=dtypes.int64)).numpy(),
)
