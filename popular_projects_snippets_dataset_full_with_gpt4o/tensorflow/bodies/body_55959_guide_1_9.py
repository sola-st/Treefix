from google.protobuf import text_format # pragma: no cover

op_def_library = type('OpDefLibraryMock', (object,), {'apply_op': lambda self, op_type, a, name: type('OpMock', (object,), {'node_def': type('NodeDefMock', (object,), {'name': name, 'op': op_type, 'attr': {'a': {'list': {'b': a}}}})()})()}) # pragma: no cover
class MockSelf: # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        expected_proto = text_format.Parse(expected, tf.compat.v1.NodeDef()) # pragma: no cover
        actual_proto = text_format.Parse(str(actual), tf.compat.v1.NodeDef()) # pragma: no cover
        assert expected_proto == actual_proto # pragma: no cover
    def assertRaises(self, exception_type): # pragma: no cover
        class ContextManagerMock: # pragma: no cover
            def __enter__(self_): # pragma: no cover
                return self_ # pragma: no cover
            def __exit__(self_, exc_type, exc_val, exc_tb): # pragma: no cover
                assert exc_type == exception_type # pragma: no cover
                return True # pragma: no cover
        return ContextManagerMock() # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b # pragma: no cover
self = MockSelf() # pragma: no cover
_l_ = lambda x: None # pragma: no cover

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
