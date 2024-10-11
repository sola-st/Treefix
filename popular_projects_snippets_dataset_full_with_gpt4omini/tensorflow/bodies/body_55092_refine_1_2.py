class extension_type: pass # pragma: no cover
class MyType(extension_type): pass # pragma: no cover
class ops: Tensor = type('Tensor', (object,), {}) # pragma: no cover
POSITIONAL_OR_KEYWORD = 1 # pragma: no cover
KEYWORD_ONLY = 2 # pragma: no cover
self = object() # pragma: no cover

import inspect as tf_inspect # pragma: no cover

class extension_type: pass # pragma: no cover
class MockExtensionType(extension_type): pass # pragma: no cover
class MyType(MockExtensionType): pass # pragma: no cover
class MockTensor: pass # pragma: no cover
POSITIONAL_OR_KEYWORD = 1 # pragma: no cover
KEYWORD_ONLY = 2 # pragma: no cover
self = type('Mock', (object,), {'assertEqual': lambda s, a, b: a == b})() # pragma: no cover
tf_inspect.Parameter = lambda name, kind, annotation=None, default=None: {'name': name, 'kind': kind, 'annotation': annotation, 'default': default} # pragma: no cover
tf_inspect.Signature = lambda parameters, return_annotation: {'parameters': parameters, 'return_annotation': return_annotation} # pragma: no cover
tf_inspect.signature = lambda obj: tf_inspect.Signature([], MyType) # pragma: no cover

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
