# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nary_ops_test.py
with self.session() as session, self.test_scope():
    indices = array_ops.constant(np.array([[2, 3], [0, 1]], dtype=np.int32))
    op = array_ops.one_hot(indices,
                           np.int32(4),
                           on_value=np.float32(7), off_value=np.float32(3))
    output = session.run(op)
    expected = np.array([[[3, 3, 7, 3], [3, 3, 3, 7]],
                         [[7, 3, 3, 3], [3, 7, 3, 3]]],
                        dtype=np.float32)
    self.assertAllEqual(output, expected)

    op = array_ops.one_hot(indices,
                           np.int32(4),
                           on_value=np.int32(2), off_value=np.int32(1),
                           axis=1)
    output = session.run(op)
    expected = np.array([[[1, 1], [1, 1], [2, 1], [1, 2]],
                         [[2, 1], [1, 2], [1, 1], [1, 1]]],
                        dtype=np.int32)
    self.assertAllEqual(output, expected)
