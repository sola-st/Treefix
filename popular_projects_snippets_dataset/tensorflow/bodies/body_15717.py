# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
test_value = [[1, 2, 3, 4, 5], [6, 7], [8, 9, 10], [], [9],
              [1, 2, 3, 4, 5, 6, 7, 8]]
rt = ragged_factory_ops.constant(test_value)
for step in [-3, -2, -1, 1, 2, 3]:
    # Slice outer dimension
    self.assertAllEqual(rt[start:stop:step], test_value[start:stop:step],
                        'slice=%s:%s:%s' % (start, stop, step))
    # Slice inner dimension
    self.assertAllEqual(rt[:, start:stop:step],
                        [row[start:stop:step] for row in test_value],
                        'slice=%s:%s:%s' % (start, stop, step))
