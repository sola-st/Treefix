# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/util_test.py
x_ = np.asarray(x_)
with self.cached_session() as sess:
    static_shape = None if use_deferred_shape else x_.shape
    x_pl = array_ops.placeholder_with_default(x_, shape=static_shape)
    # Add `zeros_like(x)` such that x's value and gradient are identical. We
    # do this so we can ensure each gradient value is mapped to the right
    # gradient location.  (Not doing this means the gradient wrt `x` is simple
    # `ones_like(x)`.)
    # Note:
    #   zeros_like_x_pl == zeros_like(x_pl)
    #   gradient(zeros_like_x_pl, x_pl) == x_pl - 1
    zeros_like_x_pl = (x_pl * array_ops.stop_gradient(x_pl - 1.)
                       - array_ops.stop_gradient(x_pl * (x_pl - 1.)))
    x = x_pl + zeros_like_x_pl
    actual = du.fill_triangular(x, **kwargs)
    grad_actual = gradients_impl.gradients(actual, x_pl)[0]
    [actual_, grad_actual_] = sess.run([actual, grad_actual],
                                       feed_dict={x_pl: x_})
expected = self._fill_triangular(x_, **kwargs)
if use_deferred_shape:
    self.assertEqual(None, actual.shape)
else:
    self.assertAllEqual(expected.shape, actual.shape)
self.assertAllClose(expected, actual_, rtol=1e-8, atol=1e-9)
self.assertAllClose(x_, grad_actual_, rtol=1e-8, atol=1e-9)
