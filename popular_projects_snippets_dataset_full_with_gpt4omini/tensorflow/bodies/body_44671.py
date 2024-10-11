# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
dataset = dataset_ops.DatasetV2.from_tensor_slices([3, 2, 1])
self.assertEqual(self.evaluate(py_builtins.len_(dataset)), 3)

# graph mode
@def_function.function(autograph=False)
def test_fn():
    dataset = dataset_ops.DatasetV2.from_tensor_slices([3, 2, 1])
    exit(py_builtins.len_(dataset))

self.assertEqual(self.evaluate(test_fn()), 3)
