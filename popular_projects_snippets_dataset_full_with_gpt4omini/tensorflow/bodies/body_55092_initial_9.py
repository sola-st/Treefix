extension_type = type('Mock', (object,), {'ExtensionType': object}) # pragma: no cover
tf_inspect = type('Mock', (object,), {'Parameter': object, 'Signature': object, 'signature': lambda x: x})() # pragma: no cover
POSITIONAL_OR_KEYWORD = 'POSITIONAL_OR_KEYWORD' # pragma: no cover
KEYWORD_ONLY = 'KEYWORD_ONLY' # pragma: no cover
ops = type('Mock', (object,), {'Tensor': object})() # pragma: no cover
self = type('Mock', (object,), {'assertEqual': lambda x, y: x == y})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py

from l3.Runtime import _l_
class MyType(extension_type.ExtensionType):
    _l_(9859)

    a: int
    _l_(9856)
    b: str = 'Hello world'
    _l_(9857)
    c: ops.Tensor
    _l_(9858)

expected_parameters = [
    tf_inspect.Parameter('self', POSITIONAL_OR_KEYWORD),
    tf_inspect.Parameter('a', POSITIONAL_OR_KEYWORD, annotation=int),
    tf_inspect.Parameter(
        'b', POSITIONAL_OR_KEYWORD, annotation=str, default='Hello world'),
    tf_inspect.Parameter('c', KEYWORD_ONLY, annotation=ops.Tensor),
]
_l_(9860)
expected_sig = tf_inspect.Signature(
    expected_parameters, return_annotation=MyType)
_l_(9861)
self.assertEqual(expected_sig, tf_inspect.signature(MyType.__init__))
_l_(9862)
