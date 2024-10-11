import unittest # pragma: no cover

class MockTestCase(unittest.TestCase): # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        assert expected.strip() == actual.strip() # pragma: no cover
self = MockTestCase() # pragma: no cover
type('MockOp', (object,), {'node_def': 'name: ''t'' op: ''AttrBoolList'' attr { key: ''a'' value { list { b: true b: false b: true } } } '})() # pragma: no cover
def mock_apply_op(op_type, a, name): # pragma: no cover
    if not all(isinstance(x, bool) for x in a): # pragma: no cover
        raise TypeError("Expected bool for argument 'a' not {}".format(a[0])) # pragma: no cover
    return type('MockOp', (object,), {'node_def': 'name: ''{}'' op: ''AttrBoolList'' attr {{ key: ''a'' value {{ list {{ b: {} }} }} }}'.format(name, ' '.join(['true' if v else 'false' for v in a]))})() # pragma: no cover

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
