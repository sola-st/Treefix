# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
values = (StructuredTensor.from_pyval([{
    "a": 3
}]), StructuredTensor.from_pyval([{
    "a": 4
}]))
actual = array_ops.concat(values, axis=0)
self.assertAllEqual(actual, [{"a": 3}, {"a": 4}])
