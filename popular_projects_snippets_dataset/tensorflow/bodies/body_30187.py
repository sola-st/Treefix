# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
tensor = [1]
self.assertEqual(dtypes.int32, self.evaluate(array_ops.size(tensor)).dtype)
self.assertEqual(
    dtypes.int64,
    self.evaluate(array_ops.size(tensor, out_type=dtypes.int64)).dtype)
