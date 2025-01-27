# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
"""Tests that positive and negative infinity sort correctly."""
supported_types = set(
    [dtypes.bfloat16.as_numpy_dtype, np.float16, np.float32, np.float64])
for dtype in supported_types.intersection(self.numeric_types):
    with self.session() as sess:
        p = array_ops.placeholder(dtype)
        with self.test_scope():
            topk = nn_ops.top_k(p, k=6)
        results = sess.run(topk, {
            p:
                np.array([1, 2, float("inf"), -float("inf"), -1, -2],
                         dtype=dtype)
        })
        self.assertAllEqual(
            np.array([float("inf"), 2.0, 1.0, -1.0, -2.0, -float("inf")],
                     dtype=dtype), results[0])
        self.assertEqual(list([2, 1, 0, 4, 5, 3]), list(results[1]))
