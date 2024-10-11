# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scan_ops_test.py
np_out = handle_options(np.cumsum, np.zeros_like, x, axis, exclusive,
                        reverse)
with self.session(), self.test_scope():
    p = array_ops.placeholder(x.dtype)
    tf_out = math_ops.cumsum(p, axis, exclusive, reverse).eval(
        feed_dict={p: x})

self.assertAllClose(np_out, tf_out)
