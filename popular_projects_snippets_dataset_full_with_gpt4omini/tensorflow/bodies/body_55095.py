# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class EmptyType(extension_type.ExtensionType):
    pass

self.assertEmpty(EmptyType._tf_extension_type_fields())
x = EmptyType()
self.assertEqual(
    repr(x), 'ExtensionTypeTest.testEmptyType.<locals>.EmptyType()')
