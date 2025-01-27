# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class MyType(extension_type.ExtensionType):
    x: ops.Tensor
    y: ops.Tensor
    z: typing.Tuple[typing.Union[int, str], ...] = [1, 'two', 3]

expected_parameters = [
    tf_inspect.Parameter('self', POSITIONAL_OR_KEYWORD),
    tf_inspect.Parameter('x', POSITIONAL_OR_KEYWORD),
    tf_inspect.Parameter('y', POSITIONAL_OR_KEYWORD),
    tf_inspect.Parameter('z', POSITIONAL_OR_KEYWORD),
]
expected_sig = tf_inspect.Signature(
    expected_parameters, return_annotation=MyType.Spec)
self.assertEqual(expected_sig, tf_inspect.signature(MyType.Spec.__init__))
