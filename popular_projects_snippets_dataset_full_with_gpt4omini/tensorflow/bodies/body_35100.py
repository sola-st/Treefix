# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x_ = np.asarray(x_)
with self.cached_session() as sess:
    static_shape = None if use_deferred_shape else x_.shape
    x_pl = array_ops.placeholder_with_default(x_, shape=static_shape)
    zeros_like_x_pl = (x_pl * array_ops.stop_gradient(x_pl - 1.)
                       - array_ops.stop_gradient(x_pl * (x_pl - 1.)))
    x = x_pl + zeros_like_x_pl
    actual = du.fill_triangular(x, **kwargs)
    inverse_actual = du.fill_triangular_inverse(actual, **kwargs)

    inverse_actual_ = sess.run(
        inverse_actual,
        feed_dict={x_pl: x_})

if use_deferred_shape:
    self.assertEqual(None, inverse_actual.shape)
else:
    self.assertAllEqual(x_.shape, inverse_actual.shape)
self.assertAllEqual(x_, inverse_actual_)
