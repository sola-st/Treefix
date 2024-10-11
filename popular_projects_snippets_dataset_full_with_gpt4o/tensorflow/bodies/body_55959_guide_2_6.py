from google.protobuf import text_format # pragma: no cover

class MockNodeDef: # pragma: no cover
    def __init__(self, name, op, attr): # pragma: no cover
        self.name = name # pragma: no cover
        self.op = op # pragma: no cover
        self.attr = attr # pragma: no cover
class MockOp: # pragma: no cover
    def __init__(self, name, op, a): # pragma: no cover
        attr = {'a': {'list': {'b': a}}} # pragma: no cover
        self.node_def = MockNodeDef(name, op, attr) # pragma: no cover
def mock_apply_op(op_type, a, name): # pragma: no cover
    if not all(isinstance(x, bool) for x in a): # pragma: no cover
        raise TypeError("Expected bool for argument 'a' not 0.") # pragma: no cover
    return MockOp(name, op_type, a) # pragma: no cover
op_def_library = type('MockOpDefLibrary', (object,), {'apply_op': mock_apply_op})() # pragma: no cover
class MockSelf: # pragma: no cover
    def assertProtoEquals(self, proto_str, proto): # pragma: no cover
        expected_proto = text_format.Parse(proto_str, node_def_pb2.NodeDef()) # pragma: no cover
        actual_proto = node_def_pb2.NodeDef() # pragma: no cover
        actual_proto.name = proto.name # pragma: no cover
        actual_proto.op = proto.op # pragma: no cover
        actual_proto.attr['a'].CopyFrom(tf.compat.v1.AttrValue(list=tf.compat.v1.AttrValue.ListValue(b=proto.attr['a']['list']['b']))) # pragma: no cover
        assert expected_proto == actual_proto, f"Expected: {expected_proto}, but got: {actual_proto}" # pragma: no cover
    def assertRaises(self, exception): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if exc_type is None: # pragma: no cover
                    raise AssertionError(f"Expected exception {exception}, but no exception was raised") # pragma: no cover
                if not issubclass(exc_type, exception): # pragma: no cover
                    raise AssertionError(f"Expected exception {exception}, but got {exc_type}") # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
    def assertEqual(self, first, second): # pragma: no cover
        assert first == second, f"Expected: {first}, but got: {second}" # pragma: no cover
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
