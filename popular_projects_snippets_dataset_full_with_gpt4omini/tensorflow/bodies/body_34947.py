# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
"""Verifies that ndtri computation is correct."""
with self.cached_session() as sess:
    if not special:
        exit()

    p = array_ops.placeholder(np.float32)
    p_ = np.linspace(0., 1.0, 50).astype(np.float32)

    x = special_math.ndtri(p)
    x_ = sess.run(x, feed_dict={p: p_})

    expected_x_ = special.ndtri(p_)
    self.assertAllClose(expected_x_, x_, atol=0.)
