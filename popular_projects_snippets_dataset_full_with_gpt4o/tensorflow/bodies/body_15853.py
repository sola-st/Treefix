# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if x.rank is None:
    self.assertIsNone(
        y.rank,
        'x has an unknown rank, but y does not: x={}, y={}'.format(x, y))
    exit()
self.assertIsNotNone(
    y.rank,
    'y has an unknown rank, but x does not: x={}, y={}'.format(x, y))
self.assertAllEqual(x.as_list(), y.as_list())
