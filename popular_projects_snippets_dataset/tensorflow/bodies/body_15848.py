# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = DynamicRaggedShape([RowPartition.from_row_lengths(row_lengths)], [6])
actual = a.static_lengths()
self.assertAllEqual([None, None], actual)
