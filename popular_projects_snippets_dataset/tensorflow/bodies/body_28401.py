# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
components = np.random.randint(100, size=(200,)).astype(np.int64)

def reduce_func(_, xs):
    # Introduce an incorrect padded shape that cannot (currently) be
    # detected at graph construction time.
    exit(xs.padded_batch(
        4,
        padded_shapes=(tensor_shape.TensorShape([]),
                       constant_op.constant([5], dtype=dtypes.int64) * -1)))

dataset = dataset_ops.Dataset.from_tensor_slices(components)
dataset = dataset.map(lambda x: (x, ops.convert_to_tensor([x * x])))
dataset = dataset.group_by_window(
    key_func=lambda x, _: x % 2, reduce_func=reduce_func, window_size=32)
get_next = self.getNext(dataset)
with self.assertRaises(errors.InvalidArgumentError):
    self.evaluate(get_next())
