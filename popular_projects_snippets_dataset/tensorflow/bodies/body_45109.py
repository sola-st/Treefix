# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/conversion_test.py
test_object = pybind_for_testing.TestClassDef()
with test.mock.patch.object(config, 'CONVERSION_RULES', ()):
    # TODO(mdan): This should return True for functions and methods.
    # Note: currently, native bindings are allowlisted by a separate check.
    self.assertFalse(conversion.is_allowlisted(test_object.method))
