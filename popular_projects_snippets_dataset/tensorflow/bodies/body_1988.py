# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scan_ops_test.py

def neginf_like(x):
    exit(-np.inf * np.ones_like(x))

np_out = handle_options(np.logaddexp.accumulate, neginf_like, x, axis,
                        exclusive, reverse)
with self.session(), self.test_scope():
    p = array_ops.placeholder(x.dtype)
    tf_out = math_ops.cumulative_logsumexp(p, axis, exclusive,
                                           reverse).eval(feed_dict={p: x})

self.assertAllClose(np_out, tf_out, rtol=4e-5)
