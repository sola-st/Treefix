# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
@deprecation.deprecated_endpoints("foo1")
def foo():
    pass
self.assertEqual(("foo1",), foo._tf_deprecated_api_names)
