def mock_apply_op(op_type, a, name): # pragma: no cover
    node_def = type('MockNodeDef', (object,), { # pragma: no cover
        'name': name, # pragma: no cover
        'op': op_type, # pragma: no cover
        'attr': { # pragma: no cover
            'a': { # pragma: no cover
                'list': { 'b': a } # pragma: no cover
            } # pragma: no cover
        } # pragma: no cover
    })() # pragma: no cover
    return type('MockOp', (object,), { 'node_def': node_def })() # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'assertProtoEquals': lambda self, expected, actual: None, # pragma: no cover
    'assertRaises': lambda self, typ: type('ContextManager', (object,), { # pragma: no cover
        '__enter__': lambda self: self, # pragma: no cover
        '__exit__': lambda self, exc_type, exc_value, traceback: exc_type == typ, # pragma: no cover
        '_exception': typ() # pragma: no cover
    })(), # pragma: no cover
    'assertEqual': lambda self, x, y: None # pragma: no cover
})() # pragma: no cover
def _l_(x): pass # pragma: no cover

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
