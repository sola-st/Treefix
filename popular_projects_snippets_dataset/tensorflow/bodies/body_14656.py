# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
self.assertAllEqual([[1.0, 1.0], [1.0, 1.0]],
                    np_array_ops.where([True], [1.0, 1.0],
                                       [[0, 0], [0, 0]]))
