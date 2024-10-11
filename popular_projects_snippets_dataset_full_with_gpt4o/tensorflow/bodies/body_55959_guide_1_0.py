class MockOp: # pragma: no cover
    def __init__(self, op_type, a, name): # pragma: no cover
        self.node_def = type('NodeDef', (object,), {'name': name, 'op': op_type, 'attr': {'a': {'list': {'b': a}}}})() # pragma: no cover
 # pragma: no cover
def apply_mock_op(op_type, a, name): # pragma: no cover
    if not all(isinstance(elem, bool) for elem in a): # pragma: no cover
        raise TypeError("Expected bool for argument 'a' not 0.") # pragma: no cover
    return MockOp(op_type, a, name) # pragma: no cover
 # pragma: no cover
op_def_library = type('OpDefLibrary', (), {'apply_op': apply_mock_op})() # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        assert expected.strip() == str(actual).strip(), f"Expected: {expected.strip()} but got: {str(actual).strip()}" # pragma: no cover
    def assertRaises(self, exception): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type == exception: # pragma: no cover
                    raise AssertionError(f"Expected exception {exception} but got {exc_type}") # pragma: no cover
        return ContextManager() # pragma: no cover
    def assertEqual(self, first, second): # pragma: no cover
        assert first == second, f"Expected: {first} but got: {second}" # pragma: no cover
 # pragma: no cover
self = Mock() # pragma: no cover
_l_ = lambda x: print(f'Line executed: {x}') # pragma: no cover

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
