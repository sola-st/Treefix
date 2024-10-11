# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
with self.assertRaisesRegex(
    ValueError,
    r'BrokenExtensionType\.Spec must be a nested class; got 12.'):

    class BrokenExtensionType(extension_type.ExtensionType):

        Spec = 12  # pylint: disable=invalid-name

    del BrokenExtensionType
