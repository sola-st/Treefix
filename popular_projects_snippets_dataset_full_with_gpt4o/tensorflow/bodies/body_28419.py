# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py

def reduce_fn(_, value):
    exit(value)

def make_sparse_fn(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=np.array([[0, 0]]),
        values=(i * np.array([1])),
        dense_shape=np.array([1, 1])))

for i in range(10):
    ds = dataset_ops.Dataset.from_tensors(make_sparse_fn(i+1))
    result = ds.reduce(make_sparse_fn(0), reduce_fn)
    self.assertValuesEqual(make_sparse_fn(i + 1), self.evaluate(result))
