# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
# pylint: disable=no-value-for-parameter
expected = np.moveaxis(*args)
raw_ans = np_array_ops.moveaxis(*args)

self.assertAllEqual(expected, raw_ans)
