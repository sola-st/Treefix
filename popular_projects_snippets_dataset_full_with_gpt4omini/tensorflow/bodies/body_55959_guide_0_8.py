import unittest # pragma: no cover

class TestAttrBoolList(unittest.TestCase): # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        self.assertEqual(expected.strip(), actual) # pragma: no cover
    def setUp(self): # pragma: no cover
        self.mock_op_def_library = type('MockOpDefLibrary', (object,), {})() # pragma: no cover
        self.mock_op_def_library.apply_op = op_def_library.apply_op # pragma: no cover
        self.op_def_library = self.mock_op_def_library # pragma: no cover
        self._l_ = lambda x: None # pragma: no cover
    def test_attr_bool_list(self): # pragma: no cover
        pass # pragma: no cover

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
