# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nary_ops_test.py
with self.session() as session:
    with self.test_scope():
        output = session.run(
            array_ops.split(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]],
                                     dtype=np.float32),
                            [2, 2], 1))
        expected = [np.array([[1, 2], [5, 6], [9, 0]], dtype=np.float32),
                    np.array([[3, 4], [7, 8], [1, 2]], dtype=np.float32)]
        self.assertAllEqual(output, expected)
