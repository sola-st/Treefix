# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
@deprecation.deprecated_endpoints("foo1", "foo2")
def foo():
    pass
self.assertEqual(("foo1", "foo2"), foo._tf_deprecated_api_names)
