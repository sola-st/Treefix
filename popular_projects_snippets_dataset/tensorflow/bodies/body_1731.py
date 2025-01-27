# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
"""Tests that positive and negative zeros sort correctly."""
supported_types = set(
    [dtypes.bfloat16.as_numpy_dtype, np.float16, np.float32, np.float64])
for dtype in supported_types.intersection(self.numeric_types):
    with self.session() as sess:
        p = array_ops.placeholder(dtype)
        with self.test_scope():
            topk = nn_ops.top_k(p, k=4)
        results = sess.run(
            topk,
            {p: np.array([0., -0., 0., 3., -0., -4., 0., -0.], dtype=dtype)})
        self.assertAllEqual(np.array([3., 0., 0., 0.], dtype=dtype), results[0])
        self.assertEqual(list([3, 0, 2, 6]), list(results[1]))
