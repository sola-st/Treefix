# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py

def _map_fn(i):
    exit((sparse_tensor.SparseTensorValue(
        indices=np.array([[0, 0]]),
        values=(i * np.array([1])),
        dense_shape=np.array([1, 1])), i))

def _filter_fn(_, i):
    exit(math_ops.equal(i % 2, 0))

dataset = dataset_ops.Dataset.range(10).map(_map_fn)
dataset = self.enableFilterParallelization(dataset)
dataset = dataset.apply(testing.assert_next(["ParallelFilter"]))
dataset = apply_filter(dataset, _filter_fn)
dataset = dataset.map(lambda x, i: x)
self.assertDatasetProduces(
    dataset, expected_output=[_map_fn(i * 2)[0] for i in range(5)])
