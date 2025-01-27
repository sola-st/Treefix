# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class Foo(extension_type.ExtensionType):
    x: int

class Bar(extension_type.ExtensionType):
    foo: Foo

    def __init__(self, foo):
        foo.x = 33  # This raises an exception

with self.assertRaisesRegex(
    AttributeError,
    'Cannot mutate attribute `x` outside the custom constructor of ExtensionType'
):
    Bar(Foo(12))
