# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
A, B = ForwardRefA, ForwardRefB

self.assertEqual(A._tf_extension_type_fields(),
                 (extension_type_field.ExtensionTypeField(
                     'x', typing.Tuple[typing.Union[A, B], ...]),
                  extension_type_field.ExtensionTypeField('y', B)))
self.assertEqual(B._tf_extension_type_fields(),
                 (extension_type_field.ExtensionTypeField('z', B),
                  extension_type_field.ExtensionTypeField('n', ops.Tensor)))

# Check the signature.
expected_parameters = [
    tf_inspect.Parameter('self', POSITIONAL_OR_KEYWORD),
    tf_inspect.Parameter(
        'x',
        POSITIONAL_OR_KEYWORD,
        annotation=typing.Tuple[typing.Union['ForwardRefA', 'ForwardRefB'],
                                ...]),
    tf_inspect.Parameter(
        'y', POSITIONAL_OR_KEYWORD, annotation='ForwardRefB'),
]
expected_sig = tf_inspect.Signature(
    expected_parameters, return_annotation=A)
self.assertEqual(tf_inspect.signature(A.__init__), expected_sig)
