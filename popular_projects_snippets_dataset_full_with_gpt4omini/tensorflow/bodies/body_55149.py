# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

class Instrument(extension_type.ExtensionType):
    name: ops.Tensor
    weight: ops.Tensor
    needs_case: bool

class StringInstrument(Instrument):
    num_strings: int  # Add a new field
    needs_case: bool = True  # Override default value.

class Violin(StringInstrument):
    maker: ops.Tensor
    num_strings: int = 4  # Override default value.
    name: str = 'violin'  # Override field type and default value.

self.assertEqual(
    list(
        tf_inspect.signature(
            StringInstrument.__init__).parameters.values()), [
                tf_inspect.Parameter('self', POSITIONAL_OR_KEYWORD),
                tf_inspect.Parameter(
                    'name', POSITIONAL_OR_KEYWORD, annotation=ops.Tensor),
                tf_inspect.Parameter(
                    'weight', POSITIONAL_OR_KEYWORD, annotation=ops.Tensor),
                tf_inspect.Parameter(
                    'needs_case',
                    POSITIONAL_OR_KEYWORD,
                    annotation=bool,
                    default=True),
                tf_inspect.Parameter(
                    'num_strings', KEYWORD_ONLY, annotation=int),
            ])
self.assertEqual(
    list(tf_inspect.signature(Violin.__init__).parameters.values()), [
        tf_inspect.Parameter('self', POSITIONAL_OR_KEYWORD),
        tf_inspect.Parameter(
            'name', POSITIONAL_OR_KEYWORD, annotation=str,
            default='violin'),
        tf_inspect.Parameter('weight', KEYWORD_ONLY, annotation=ops.Tensor),
        tf_inspect.Parameter(
            'needs_case', KEYWORD_ONLY, annotation=bool, default=True),
        tf_inspect.Parameter(
            'num_strings', KEYWORD_ONLY, annotation=int, default=4),
        tf_inspect.Parameter('maker', KEYWORD_ONLY, annotation=ops.Tensor),
    ])

violin = Violin(weight=28, maker='Amati')
self.assertAllEqual(violin.name, 'violin')
self.assertAllEqual(violin.weight, 28)
self.assertAllEqual(violin.needs_case, True)
self.assertAllEqual(violin.num_strings, 4)
self.assertAllEqual(violin.maker, 'Amati')
