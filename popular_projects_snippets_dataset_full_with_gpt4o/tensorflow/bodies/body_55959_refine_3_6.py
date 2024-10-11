import unittest # pragma: no cover

class MockTest(unittest.TestCase): # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        self.assertEqual(expected.strip(), str(actual).strip()) # pragma: no cover
 # pragma: no cover
self = MockTest() # pragma: no cover

import unittest # pragma: no cover

class MockSelf(unittest.TestCase): # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        expected_proto = tf.compat.v1.protobuf.text_format.Parse(expected, tf.compat.v1.NodeDef()) # pragma: no cover
        self.assertEqual(expected_proto, actual) # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

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
