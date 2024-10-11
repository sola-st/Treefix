from google.protobuf import text_format # pragma: no cover

_l_ = lambda x: None # pragma: no cover
class MockTest: # pragma: no cover
    def assertProtoEquals(self, proto_str, actual_proto): # pragma: no cover
        expected_proto = text_format.Parse(proto_str, tf.compat.v1.NodeDef()) # pragma: no cover
        assert expected_proto == actual_proto # pragma: no cover
    def assertRaises(self, exception): # pragma: no cover
        class ContextManagerMock: # pragma: no cover
            def __enter__(nonlocal_self): # pragma: no cover
                return nonlocal_self # pragma: no cover
            def __exit__(nonlocal_self, exc_type, exc_value, traceback): # pragma: no cover
                assert exc_type is exception # pragma: no cover
                return True # pragma: no cover
        return ContextManagerMock() # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b # pragma: no cover
self = MockTest() # pragma: no cover
def apply_op(name, a, name_str): # pragma: no cover
    class NodeDefMock: # pragma: no cover
        def __init__(self, name, op, attr): # pragma: no cover
            self.name = name # pragma: no cover
            self.op = op # pragma: no cover
            self.attr = {'a': {'list': {'b': attr}}} # pragma: no cover
    if not all(isinstance(i, bool) for i in a): # pragma: no cover
        raise TypeError("Expected bool for argument 'a' not {}.".format(type(a[0]).__name__)) # pragma: no cover
    return NodeDefMock(name_str, name, a) # pragma: no cover
op_def_library = type('MockOpDefLibrary', (object,), {'apply_op': apply_op})() # pragma: no cover

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
