# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/quantized_ops_test.py
with self.session() as session:
    for dtype in self.quantized_tf_types:
        in_values = np.array([1, 2, 3, 4, 5, 6])
        expected = [[1, 2], [3, 4], [5, 6]]
        with self.test_scope():
            p = array_ops.placeholder(dtype=dtypes.int32)
            x = math_ops.cast(p, dtype)
            x = array_ops.reshape(x, [3, 2])

        value = session.run(x, {p: in_values})
        self.assertAllEqual(value, expected)
