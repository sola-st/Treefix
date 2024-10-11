import unittest # pragma: no cover

class TestAttrBoolListOp(unittest.TestCase): # pragma: no cover
    def assertProtoEquals(self, expected_proto, actual_proto): # pragma: no cover
        self.assertEqual(expected_proto.strip(), actual_proto) # pragma: no cover
    def test_attr_bool_list(self): # pragma: no cover
        self.assertTrue(True) # pragma: no cover
        ops.Graph().as_default() # pragma: no cover
        class MockOpDefLibrary: # pragma: no cover
            @staticmethod # pragma: no cover
            def apply_op(op_name, a, name): # pragma: no cover
                return type('Op', (object,), {'node_def': 'name: ' + repr(name) + ' op: ' + repr(op_name) + ' attr { key: ' + repr('a') + ' value { list { ' + ' '.join(['b: ' + str(x) for x in a]) + ' } } }' })() # pragma: no cover
        global op_def_library # pragma: no cover
        op_def_library = MockOpDefLibrary() # pragma: no cover
        mock_self = type('MockSelf', (object,), {'assertProtoEquals': self.assertProtoEquals})() # pragma: no cover
        self = mock_self # pragma: no cover

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
