# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/bijector_test.py
x_ = [[[1., 2.], [3., 4.]]]
x = array_ops.placeholder_with_default(x_, shape=None)
event_ndims = array_ops.placeholder(dtype=np.int32, shape=[])
bij = ExpOnlyJacobian(forward_min_event_ndims=1)
bij.inverse_log_det_jacobian(x, event_ndims=event_ndims)
with self.cached_session() as sess:
    ildj = sess.run(bij.inverse_log_det_jacobian(x, event_ndims=event_ndims),
                    feed_dict={event_ndims: 1})
self.assertAllClose(-np.log(x_), ildj)
