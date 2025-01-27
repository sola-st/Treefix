# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
with self.assertRaises(TypeError):
    type_spec.get_name(None)

class Foo(TwoCompositesSpec):
    pass

with self.assertRaisesRegex(
    ValueError, "TypeSpec __main__.Foo has not been registered."):
    type_spec.get_name(Foo)
