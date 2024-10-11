self = type('Mock', (), {'assertProtoEquals': lambda self, expected, actual: None, 'assertEqual': lambda self, first, second: None, 'assertRaises': lambda self, exception: (yield)})() # pragma: no cover
class MockGraph: # pragma: no cover
    def as_default(self): # pragma: no cover
        return self # pragma: no cover
class MockOpDefLibrary: # pragma: no cover
    def apply_op(self, op_type, **kwargs): # pragma: no cover
        return tf.Operation(name=kwargs['name'], type=op_type, device='', graph=tf.Graph()) # pragma: no cover
op_def_library = MockOpDefLibrary() # pragma: no cover

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
