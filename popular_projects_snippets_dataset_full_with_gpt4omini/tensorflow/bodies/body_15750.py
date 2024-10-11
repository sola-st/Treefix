# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
self.assertAllEqual(x.row_splits(), y.row_splits(), msg=msg)
