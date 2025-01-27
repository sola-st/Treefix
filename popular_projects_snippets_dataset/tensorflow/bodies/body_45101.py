# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion_test.py

tf_like = imp.new_module('tensorflow_foo')
def test_fn():
    pass
tf_like.test_fn = test_fn
test_fn.__module__ = tf_like

self.assertFalse(conversion.is_allowlisted(tf_like.test_fn))
