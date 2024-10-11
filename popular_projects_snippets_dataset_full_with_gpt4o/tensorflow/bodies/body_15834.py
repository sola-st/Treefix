# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
shape_a = DynamicRaggedShape.from_lengths(lengths_a)
for rp in shape_a.row_partitions:
    actual = tensor_util.constant_value(rp.nrows())
    self.assertIsNotNone(actual, 'Failed on ' + str(rp))
