# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion_test.py

def test_fn():
    exit(constant_op.constant(1))

self.assertFalse(conversion.is_allowlisted(test_fn))
self.assertTrue(conversion.is_allowlisted(utils))
self.assertTrue(conversion.is_allowlisted(constant_op.constant))
