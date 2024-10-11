from google.protobuf import text_format # pragma: no cover

def mock_apply_op(op_type, a, name): # pragma: no cover
    if not all(isinstance(x, bool) for x in a): # pragma: no cover
        raise TypeError("Expected bool for argument 'a' not 0.") # pragma: no cover
    node_def_str = f"name: '{name}' op: '{op_type}' attr {{ key: 'a' value {{ list {{ {' '.join([f'b: {str(x).lower()}' for x in a])} }} }} }}" # pragma: no cover
    node_def = text_format.Parse(node_def_str, tf.compat.v1.NodeDef()) # pragma: no cover
    return type('MockOp', (object,), {'node_def': node_def})() # pragma: no cover
op_def_library = type('MockOpDefLibrary', (object,), {'apply_op': mock_apply_op})() # pragma: no cover
class MockSelf: # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        expected_proto = text_format.Parse(expected, tf.compat.v1.NodeDef()) # pragma: no cover
        assert expected_proto == actual, f"Expected {expected_proto}, but got {actual}" # pragma: no cover
    def assertRaises(self, exception_type): # pragma: no cover
        class ContextManagerMock: # pragma: no cover
            def __enter__(self_): return self_ # pragma: no cover
            def __exit__(self_, exc_type, exc_val, exc_tb): # pragma: no cover
                assert exc_type == exception_type, f"Expected {exception_type}, but got {exc_type}" # pragma: no cover
                return True # pragma: no cover
        return ContextManagerMock() # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b, f"Expected {a}, but got {b}" # pragma: no cover
self = MockSelf() # pragma: no cover
def _l_(x): pass # pragma: no cover

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
