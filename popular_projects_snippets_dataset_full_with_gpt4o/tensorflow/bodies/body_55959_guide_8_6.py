from google.protobuf import text_format # pragma: no cover

class MockOpDefLibrary: # pragma: no cover
    def apply_op(self, op_type, a, name): # pragma: no cover
        if not all(isinstance(item, bool) for item in a): # pragma: no cover
            raise TypeError(f"Expected bool for argument 'a' not {a[0]}.") # pragma: no cover
        node_def = node_def_pb2.NodeDef( # pragma: no cover
            name=name, op=op_type, attr={'a': node_def_pb2.AttrValue(list=node_def_pb2.AttrValue.ListValue(b=a))}) # pragma: no cover
        return type('MockOp', (object,), {'node_def': node_def})() # pragma: no cover
op_def_library = MockOpDefLibrary() # pragma: no cover
class MockSelf: # pragma: no cover
    def assertProtoEquals(self, proto_str, proto): # pragma: no cover
        expected_proto = text_format.Parse(proto_str.strip(), node_def_pb2.NodeDef()) # pragma: no cover
        if expected_proto != proto: # pragma: no cover
            raise AssertionError(f'Expected: {expected_proto}, but got: {proto}') # pragma: no cover
    def assertRaises(self, exception_type): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                self.exception = None # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                self.exception = exc_value if exc_type == exception_type else None # pragma: no cover
                return exc_type == exception_type # pragma: no cover
        return ContextManager() # pragma: no cover
    def assertEqual(self, first, second): # pragma: no cover
        if first != second: # pragma: no cover
            raise AssertionError(f'Expected: {first}, but got: {second}') # pragma: no cover
self = MockSelf() # pragma: no cover
def _l_(x): print(f'Line executed: {x}') # pragma: no cover

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
