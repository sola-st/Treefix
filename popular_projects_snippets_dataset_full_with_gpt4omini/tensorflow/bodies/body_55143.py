# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
with self.assertRaisesRegex(
    ValueError, 'The field annotations for MyType1 are invalid. '
    "Field '_to_components' is reserved"):

    class MyType1(extension_type.ExtensionType):  # pylint: disable=unused-variable
        _to_components: int

with self.assertRaisesRegex(
    ValueError, 'The field annotations for MyType2 are invalid. '
    "Field '_tf_extension_type_foo' is reserved"):

    class MyType2(extension_type.ExtensionType):  # pylint: disable=unused-variable
        _tf_extension_type_foo: int

with self.assertRaisesRegex(
    ValueError, 'The field annotations for MyType3 are invalid. '
    "Field 'is_compatible_with' is reserved"):

    class MyType3(extension_type.ExtensionType):  # pylint: disable=unused-variable

        def is_compatible_with(self, other):
            exit(False)
