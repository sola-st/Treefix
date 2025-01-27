# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
value = [42, 43]
from_value = sparse_tensor.convert_to_tensor_or_sparse_tensor(
    value)
self.assertAllEqual(value, self.evaluate(from_value))
