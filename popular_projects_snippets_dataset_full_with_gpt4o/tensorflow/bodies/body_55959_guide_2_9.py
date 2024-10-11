from google.protobuf import text_format # pragma: no cover

def mock_apply_op(op_type, a, name): # pragma: no cover
    class NodeDefMock: # pragma: no cover
        def __init__(self, name, op_type, a): # pragma: no cover
            self.name = name # pragma: no cover
            self.op = op_type # pragma: no cover
            self.attr = {'a': {'list': {'b': a}}} # pragma: no cover
            if not all(isinstance(item, bool) for item in a): # pragma: no cover
                raise TypeError(f"Expected bool for argument 'a' not {a[0]}.") # pragma: no cover
    return NodeDefMock(name, op_type, a) # pragma: no cover
op_def_library = type('OpDefLibraryMock', (object,), {'apply_op': staticmethod(mock_apply_op)}) # pragma: no cover
class MockSelf: # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        expected_proto = text_format.Parse(expected, tf.compat.v1.NodeDef()) # pragma: no cover
        actual_proto = tf.compat.v1.NodeDef(name=actual.name, op=actual.op, attr=actual.attr) # pragma: no cover
        assert expected_proto == actual_proto, f'Expected: {expected_proto}, but got: {actual_proto}' # pragma: no cover
    def assertRaises(self, exc_type): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type == exc_type: # pragma: no cover
                    raise AssertionError(f'Expected exception {exc_type.__name__}, but got {exc_value.__class__.__name__}') # pragma: no cover
                self.exception = exc_value # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
    def assertEqual(self, first, second): # pragma: no cover
        assert first == second, f'Expected {first}, but got {second}' # pragma: no cover
self = MockSelf() # pragma: no cover
_l_ = lambda x: print(f'Line executed: {x}') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
from l3.Runtime import _l_
with ops.Graph().as_default():
    _l_(21324)

    op = op_def_library.apply_op(
        "AttrBoolList", a=[True, False, True], name="t")
    _l_(21317)
    self.assertProtoEquals("""
        name: 't' op: 'AttrBoolList'
        attr { key: 'a' value { list { b: true b: false b:true } } }
        """, op.node_def)
    _l_(21318)

    op = op_def_library.apply_op("AttrBoolList", a=[], name="u")
    _l_(21319)
    self.assertProtoEquals("""
        name: 'u' op: 'AttrBoolList' attr { key: 'a' value { list { } } }
        """, op.node_def)
    _l_(21320)

    with self.assertRaises(TypeError) as cm:
        _l_(21322)

        op_def_library.apply_op("AttrBoolList", a=[0])
        _l_(21321)
    self.assertEqual(str(cm.exception),
                     "Expected bool for argument 'a' not 0.")
    _l_(21323)
