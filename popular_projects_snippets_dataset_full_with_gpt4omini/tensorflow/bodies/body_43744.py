# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation_test.py
with self.assertRaises(deprecation.DeprecatedNamesAlreadySet):
    @deprecation.deprecated_endpoints("foo1")
    @deprecation.deprecated_endpoints("foo2")
    def foo():  # pylint: disable=unused-variable
        pass
