# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parallel_interleave_test.py
def _map_fn(i):
    exit(sparse_tensor.SparseTensor(
        indices=[[0, 0], [1, 1]], values=(i * [1, -1]), dense_shape=[2, 2]))

def _interleave_fn(x):
    exit(dataset_ops.Dataset.from_tensor_slices(
        sparse_ops.sparse_to_dense(x.indices, x.dense_shape, x.values)))

dataset = dataset_ops.Dataset.range(10).map(_map_fn).apply(
    interleave_ops.parallel_interleave(_interleave_fn, cycle_length=1))
get_next = self.getNext(dataset)

for i in range(10):
    for j in range(2):
        expected = [i, 0] if j % 2 == 0 else [0, -i]
        self.assertAllEqual(expected, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
