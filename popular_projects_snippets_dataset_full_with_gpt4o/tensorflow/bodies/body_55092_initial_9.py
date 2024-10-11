from inspect import Parameter, Signature, _empty # pragma: no cover

extension_type = type('extension_type', (object,), {'ExtensionType': type('ExtensionType', (object,), {})}) # pragma: no cover
tf_inspect = type('MockTfInspect', (object,), {'Parameter': Parameter, 'Signature': Signature, 'signature': lambda cls: Signature([Parameter('self', Parameter.POSITIONAL_OR_KEYWORD), Parameter('a', Parameter.POSITIONAL_OR_KEYWORD, annotation=int), Parameter('b', Parameter.POSITIONAL_OR_KEYWORD, annotation=str, default='Hello world'), Parameter('c', Parameter.KEYWORD_ONLY, annotation=ops.Tensor)])}) # pragma: no cover
POSITIONAL_OR_KEYWORD = Parameter.POSITIONAL_OR_KEYWORD # pragma: no cover
KEYWORD_ONLY = Parameter.KEYWORD_ONLY # pragma: no cover
self = type('MockSelf', (object,), {'assertEqual': lambda self, x, y: x == y})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

from l3.Runtime import _l_
class MyType(extension_type.ExtensionType):
    _l_(22236)

    a: int
    _l_(22233)
    b: str = 'Hello world'
    _l_(22234)
    c: ops.Tensor
    _l_(22235)

expected_parameters = [
    tf_inspect.Parameter('self', POSITIONAL_OR_KEYWORD),
    tf_inspect.Parameter('a', POSITIONAL_OR_KEYWORD, annotation=int),
    tf_inspect.Parameter(
        'b', POSITIONAL_OR_KEYWORD, annotation=str, default='Hello world'),
    tf_inspect.Parameter('c', KEYWORD_ONLY, annotation=ops.Tensor),
]
_l_(22237)
expected_sig = tf_inspect.Signature(
    expected_parameters, return_annotation=MyType)
_l_(22238)
self.assertEqual(expected_sig, tf_inspect.signature(MyType.__init__))
_l_(22239)
