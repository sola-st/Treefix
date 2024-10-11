self = type('MockSelf', (object,), {'assertProtoEquals': lambda self, x, y: None, 'assertRaises': lambda self, exc_type: tf.test.TestCase.assertRaises(tf.test.TestCase(), exc_type), 'assertEqual': lambda self, x, y: None})() # pragma: no cover

import unittest # pragma: no cover

class MockSelf:# pragma: no cover
    def assertProtoEquals(self, proto_str, node_def):# pragma: no cover
        expected_proto = tf.compat.v1.protobuf.text_format.Parse(proto_str, tf.compat.v1.NodeDef())# pragma: no cover
        if expected_proto != node_def:# pragma: no cover
            raise AssertionError(f'Protos do not match: {expected_proto} != {node_def}')# pragma: no cover
    def assertRaises(self, exc_type):# pragma: no cover
        return unittest.TestCase.assertRaises(self, exc_type)# pragma: no cover
    def assertEqual(self, x, y):# pragma: no cover
        if x != y:# pragma: no cover
            raise AssertionError(f'{x} != {y}') # pragma: no cover
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
