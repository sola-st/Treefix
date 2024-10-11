# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scan_ops_test.py
np_out = handle_options(np.cumprod, np.ones_like, x, axis, exclusive,
                        reverse)
with self.session(), self.test_scope():
    p = array_ops.placeholder(x.dtype)
    prod = math_ops.cumprod(p, axis, exclusive, reverse)
    tf_out = prod.eval(feed_dict={p: x})

self.assertAllClose(np_out, tf_out)
