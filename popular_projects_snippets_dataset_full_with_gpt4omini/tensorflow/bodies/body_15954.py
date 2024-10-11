# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_util_test.py
result = ragged_util.repeat(data, repeats, axis)
self.assertAllEqual(result, expected)
