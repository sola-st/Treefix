type("Mock", (object,), {"assertProtoEquals": lambda self, x, y: None, "assertRaises": lambda self, exc: type("Context", (object,), {"__enter__": lambda self: self, "__exit__": lambda self, typ, val, tb: None}), "assertEqual": lambda self, x, y: None}) # pragma: no cover

type("Mock", (object,), {"assertProtoEquals": lambda self, x, y: None, "assertRaises": lambda self, exc: type("Context", (object,), {"__enter__": lambda self: self, "__exit__": lambda self, typ, val, tb: None}), "assertEqual": lambda self, x, y: None}) # pragma: no cover
self = type('Mock', (object,), {"assertProtoEquals": lambda self, x, y: None, "assertRaises": lambda self, exc: type('Context', (object,), {'__enter__': lambda self: self, '__exit__': lambda self, typ, val, tb: None}), "assertEqual": lambda self, x, y: None})() # pragma: no cover
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
