# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives_test.py
# Note: seems that any exception raised here is absorbed by hasattr.
# So we can't call test.fail or raise.
self.getattr_called = True
