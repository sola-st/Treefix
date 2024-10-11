from google.protobuf.any_pb2 import Any # pragma: no cover
import unittest # pragma: no cover

class MockOpDefLibrary: # pragma: no cover
    @staticmethod # pragma: no cover
    def apply_op(op_type, a, name): # pragma: no cover
        if not all(isinstance(item, bool) for item in a): # pragma: no cover
            raise TypeError("Expected bool for argument 'a' not 0.") # pragma: no cover
        node_def = NodeDef() # pragma: no cover
        node_def.name = name # pragma: no cover
        node_def.op = op_type # pragma: no cover
        attr_value = node_def.attr['a'] # pragma: no cover
        attr_value.list.b.extend(a) # pragma: no cover
        return type('MockOp', (object,), {'node_def': node_def})() # pragma: no cover
op_def_library = MockOpDefLibrary() # pragma: no cover
 # pragma: no cover
class MockTestCase(unittest.TestCase): # pragma: no cover
    def assertProtoEquals(self, expected_proto_str, actual_proto): # pragma: no cover
        expected_proto = NodeDef() # pragma: no cover
        text_format.Parse(expected_proto_str, expected_proto) # pragma: no cover
        self.assertEqual(expected_proto, actual_proto) # pragma: no cover
 # pragma: no cover
    def runTest(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
    def assertRaises(self, exc): # pragma: no cover
        context_manager = super().assertRaises(exc) # pragma: no cover
        context_manager.__exit__ = lambda *args: exc is args[0] # pragma: no cover
        return context_manager # pragma: no cover
 # pragma: no cover
self = MockTestCase() # pragma: no cover
_l_ = lambda x: print(f"Line executed: {x}") # pragma: no cover

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
