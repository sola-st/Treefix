_l_ = lambda x: None # pragma: no cover
def apply_op_mock(op_type, a, name): # pragma: no cover
    node_def = type('NodeDef', (object,), {})() # pragma: no cover
    node_def.name = name # pragma: no cover
    node_def.op = op_type # pragma: no cover
    node_def.attr = {'a': {'list': {'b': a}}} # pragma: no cover
    return type('Operation', (object,), {'node_def': node_def})() # pragma: no cover
op_def_library = type('OpDefLibrary', (object,), {'apply_op': apply_op_mock})() # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'assertProtoEquals': lambda self, x, y: print('assertProtoEquals called'), # pragma: no cover
    'assertRaises': lambda self, exc_type: type('ContextManager', (object,), { # pragma: no cover
        '__enter__': lambda self: self, # pragma: no cover
        '__exit__': lambda self, exc_type, exc_value, traceback: isinstance(exc_value, TypeError), # pragma: no cover
        'exception': TypeError('Expected bool for argument a not 0.') # pragma: no cover
    })(), # pragma: no cover
    'assertEqual': lambda self, x, y: print('assertEqual called' if x == y else 'assertEqual failed') # pragma: no cover
})() # pragma: no cover

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
