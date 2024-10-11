class MockExtensionType(type('MockBase', (object,), {})): pass # pragma: no cover
extension_type = MockExtensionType # pragma: no cover
self = type('Mock', (object,), {'assertEqual': lambda self, x, y: None})() # pragma: no cover

class MockExtensionType(type('MockBase', (object,), {})): pass # pragma: no cover
class ExtensionTypeBase: pass # pragma: no cover
self = type('Mock', (object,), {'assertEqual': lambda self, x, y: None})() # pragma: no cover

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
