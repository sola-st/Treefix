import inspect as tf_inspect # pragma: no cover

extension_type = type('Mock', (object,), {'ExtensionType': object}) # pragma: no cover
tf_inspect = type('Mock', (object,), {'Parameter': lambda name, kind, annotation=None, default=None: {'name': name, 'kind': kind, 'annotation': annotation, 'default': default}, 'Signature': lambda parameters, return_annotation: {'parameters': parameters, 'return_annotation': return_annotation}, 'signature': lambda obj: {'parameters': obj.__init__.__code__.co_varnames, 'return_annotation': MyType}})() # pragma: no cover
POSITIONAL_OR_KEYWORD = 'POS'  # Placeholder for parameter kind # pragma: no cover
KEYWORD_ONLY = 'KEY'  # Placeholder for parameter kind # pragma: no cover
ops = type('Mock', (object,), {'Tensor': object}) # pragma: no cover
self = type('Mock', (object,), {'assertEqual': lambda self, a, b: a == b})() # pragma: no cover

import inspect as tf_inspect # pragma: no cover

class MockExtensionType(object): pass # pragma: no cover
extension_type = type('Mock', (object,), {'ExtensionType': MockExtensionType})() # pragma: no cover
tf_inspect = type('Mock', (object,), {'Parameter': lambda name, kind, **kwargs: (name, kind, kwargs), 'Signature': lambda parameters, return_annotation: (parameters, return_annotation), 'signature': lambda obj: {'parameters': obj.__init__.__code__.co_varnames, 'return_annotation': obj.__init__.__annotations__.get('return', None)}})() # pragma: no cover
POSITIONAL_OR_KEYWORD = 1  # Mimicking an enum value # pragma: no cover
KEYWORD_ONLY = 2  # Mimicking an enum value # pragma: no cover
ops = type('Mock', (object,), {'Tensor': object})() # pragma: no cover
class MockSelf:  # Recreating the assertEqual method for testing # pragma: no cover
    def assertEqual(self, a, b): return a == b # pragma: no cover
self = MockSelf() # pragma: no cover

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
