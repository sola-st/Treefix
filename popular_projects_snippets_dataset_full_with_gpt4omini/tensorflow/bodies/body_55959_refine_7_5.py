class Mock: pass # pragma: no cover
ops = type('MockOps', (object,), {'Graph': staticmethod(lambda: Mock()), 'apply_op': staticmethod(lambda op_name, a, name: Mock())})() # pragma: no cover
op_def_library = type('Mock', (object,), {'apply_op': staticmethod(lambda op_name, a, name: Mock())})() # pragma: no cover
self = type('MockSelf', (object,), {'assertProtoEquals': lambda self, expected, actual: None, 'assertRaises': lambda self, exc: mock_context_manager(exc), 'assertEqual': lambda self, first, second: None})() # pragma: no cover
def mock_context_manager(exc_type): return type('MockContext', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_value, traceback: True})() # pragma: no cover

class MockGraph:# pragma: no cover
    def as_default(self): return self# pragma: no cover
# pragma: no cover
class MockOpDefLibrary:# pragma: no cover
    def apply_op(self, op_name, **kwargs):# pragma: no cover
        return type('MockOp', (), {'node_def': kwargs})()# pragma: no cover
# pragma: no cover
ops = type('MockOps', (), {'Graph': MockGraph})()# pragma: no cover
# pragma: no cover
op_def_library = MockOpDefLibrary()# pragma: no cover
# pragma: no cover
class MockSelf:# pragma: no cover
    def assertProtoEquals(self, expected, actual): pass# pragma: no cover
    def assertRaises(self, exception): return contextlib.nullcontext()# pragma: no cover
    def assertEqual(self, first, second): pass# pragma: no cover
# pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
from l3.Runtime import _l_
with ops.Graph().as_default():
    _l_(8558)

    op = op_def_library.apply_op(
        "AttrBoolList", a=[True, False, True], name="t")
    _l_(8551)
    self.assertProtoEquals("""
        name: 't' op: 'AttrBoolList'
        attr { key: 'a' value { list { b: true b: false b:true } } }
        """, op.node_def)
    _l_(8552)

    op = op_def_library.apply_op("AttrBoolList", a=[], name="u")
    _l_(8553)
    self.assertProtoEquals("""
        name: 'u' op: 'AttrBoolList' attr { key: 'a' value { list { } } }
        """, op.node_def)
    _l_(8554)

    with self.assertRaises(TypeError) as cm:
        _l_(8556)

        op_def_library.apply_op("AttrBoolList", a=[0])
        _l_(8555)
    self.assertEqual(str(cm.exception),
                     "Expected bool for argument 'a' not 0.")
    _l_(8557)
