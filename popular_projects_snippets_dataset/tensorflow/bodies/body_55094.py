# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class MyType(extension_type.ExtensionType):
    a: typing_extensions.Annotated[ops.Tensor, 'metadata']
    b: typing_extensions.Annotated[str, 'metadata'] = 'Hello world'
    c: typing.Optional[typing_extensions.Annotated[int, 'metadata']] = None

expected_parameters = [
    tf_inspect.Parameter('self', POSITIONAL_OR_KEYWORD),
    tf_inspect.Parameter('a', POSITIONAL_OR_KEYWORD, annotation=ops.Tensor),
    tf_inspect.Parameter(
        'b', POSITIONAL_OR_KEYWORD, annotation=str, default='Hello world'),
    tf_inspect.Parameter(
        'c',
        POSITIONAL_OR_KEYWORD,
        annotation=typing.Optional[int],
        default=None),
]
expected_sig = tf_inspect.Signature(
    expected_parameters, return_annotation=MyType)
self.assertEqual(expected_sig, tf_inspect.signature(MyType.__init__))
