# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scatter_nd_ops_test.py
indices = constant_op.constant([[4], [3], [1], [7]], dtype=dtypes.int32)
updates = constant_op.constant(["four", "three", "one", "seven"],
                               dtype=dtypes.string)
expected = np.array(
    [b"", b"one", b"", b"three", b"four", b"", b"", b"seven"])
scatter = self.scatter_nd(indices, updates, shape=(8,))
with self.cached_session() as sess:
    result = self.evaluate(scatter)
    self.assertAllEqual(expected, result)

# Same indice is updated twice by same value.
indices = constant_op.constant([[4], [3], [3], [7]], dtype=dtypes.int32)
updates = constant_op.constant(["a", "b", "b", "c"], dtype=dtypes.string)
expected = np.array([b"", b"", b"", b"bb", b"a", b"", b"", b"c"])
scatter = self.scatter_nd(indices, updates, shape=(8,))
with self.cached_session() as sess:
    result = self.evaluate(scatter)
    self.assertAllEqual(expected, result)

# Same indice is updated twice by different value.
indices = constant_op.constant([[4], [3], [3], [7]], dtype=dtypes.int32)
updates = constant_op.constant(["a", "b", "c", "d"], dtype=dtypes.string)
expected = [
    np.array([b"", b"", b"", b"bc", b"a", b"", b"", b"d"]),
    np.array([b"", b"", b"", b"cb", b"a", b"", b"", b"d"])
]
scatter = self.scatter_nd(indices, updates, shape=(8,))
with self.cached_session() as sess:
    result = self.evaluate(scatter)
    self.assertTrue(
        np.array_equal(result, expected[0]) or
        np.array_equal(result, expected[1]))
