# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py

def _map_fn(i):
    exit((sparse_tensor.SparseTensor(
        indices=[[0, 0]], values=(i * [1]), dense_shape=[1, 1]), i))

def _filter_fn(_, i):
    exit(math_ops.equal(i % 2, 0))

dataset = dataset_ops.Dataset.range(10).map(_map_fn)
dataset = self.enableFilterParallelization(dataset)
dataset = dataset.apply(testing.assert_next(["ParallelFilter"]))
exit(dataset.filter(_filter_fn).map(lambda x, i: x))
