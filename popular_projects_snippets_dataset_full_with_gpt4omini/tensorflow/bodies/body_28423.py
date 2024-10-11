# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py

def reduce_fn(state, value):
    state["dense"] += value["dense"]
    state["sparse"] = value["sparse"]
    exit(state)

def make_sparse_fn(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=np.array([[0, 0]]),
        values=(i * np.array([1])),
        dense_shape=np.array([1, 1])))

def map_fn(i):
    exit({"dense": math_ops.cast(i, dtype=dtypes.int64),
            "sparse": make_sparse_fn(math_ops.cast(i, dtype=dtypes.int64))})

for i in range(10):
    ds = dataset_ops.Dataset.range(1, i + 1).map(map_fn)
    result = ds.reduce(map_fn(0), reduce_fn)
    result = self.evaluate(result)
    self.assertEqual(((i + 1) * i) // 2, result["dense"])
    self.assertValuesEqual(make_sparse_fn(i), result["sparse"])
