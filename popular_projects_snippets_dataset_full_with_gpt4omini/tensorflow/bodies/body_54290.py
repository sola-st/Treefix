# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.cached_session():
    c = constant_op.constant(1)
    self.assertEqual(c._shape_tuple(), ())  # pylint: disable=protected-access
