# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ensure_shape_op_test.py
with self.session() as sess:
    p = array_ops.placeholder(dtypes.int32)
    with self.test_scope():
        op = check_ops.ensure_shape(p, (None, 3))
    expected_out = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    self.assertAllEqual(expected_out,
                        sess.run(op, {p: [[0, 1, 2], [3, 4, 5], [6, 7, 8]]}))
