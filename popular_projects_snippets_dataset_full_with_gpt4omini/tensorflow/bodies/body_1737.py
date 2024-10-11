# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/bucketize_op_test.py
with self.session() as sess:
    p = array_ops.placeholder(dtypes.float32)
    with self.test_scope():
        op = math_ops._bucketize(p, boundaries=[0, 3, 8, 11])
    expected_out = [[0, 1, 1, 2, 2], [3, 3, 4, 4, 1]]
    self.assertAllEqual(
        expected_out, sess.run(op,
                               {p: [[-5, 0, 2, 3, 5], [8, 10, 11, 12, 0]]}))
