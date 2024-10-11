# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
with self.assertRaisesRegex(
    TypeError, "In field 'values': Unsupported type annotation"):

    class MyType1(extension_type.ExtensionType):  # pylint: disable=unused-variable
        values: typing.List[ops.Tensor]

with self.assertRaisesRegex(TypeError,
                            "In field 'xyz': Unsupported type annotation"):

    class MyType2(extension_type.ExtensionType):  # pylint: disable=unused-variable
        xyz: typing.Union[typing.Tuple[complex, ...], int]
