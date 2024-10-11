# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/ext_slice_test.py
exit(n[:, tf.newaxis] - n[tf.newaxis, :])
