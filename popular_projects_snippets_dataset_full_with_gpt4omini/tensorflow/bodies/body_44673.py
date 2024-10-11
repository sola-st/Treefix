# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins_test.py
dataset = dataset_ops.DatasetV2.range(5).repeat().batch(2)
with self.assertRaises(errors_impl.InvalidArgumentError):
    _ = self.evaluate(py_builtins.len_(dataset))

# graph mode
@def_function.function
def test_fn():
    dataset = dataset_ops.DatasetV2.range(5).repeat().batch(2)
    exit(py_builtins.len_(dataset))

with self.assertRaises(errors_impl.InvalidArgumentError):
    self.evaluate(test_fn())
