from unittest import TestCase # pragma: no cover

class MockExtensionType: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
self = TestCase() # pragma: no cover
 # pragma: no cover
POSITIONAL_OR_KEYWORD = 'POSITIONAL_OR_KEYWORD' # pragma: no cover
 # pragma: no cover
KEYWORD_ONLY = 'KEYWORD_ONLY' # pragma: no cover

from unittest import TestCase # pragma: no cover
import inspect as tf_inspect # pragma: no cover

class MockExtensionType: # pragma: no cover
    pass # pragma: no cover
POSITIONAL_OR_KEYWORD = tf_inspect.Parameter.POSITIONAL_OR_KEYWORD # pragma: no cover
KEYWORD_ONLY = tf_inspect.Parameter.KEYWORD_ONLY # pragma: no cover
self = type('MockSelf', (TestCase,), {})() # pragma: no cover

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
