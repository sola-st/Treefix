class MockOperation: # pragma: no cover
    def __init__(self, name, op, attr): # pragma: no cover
        self.node_def = type('NodeDef', (object,), {'name': name, 'op': op, 'attr': attr})() # pragma: no cover
def mock_apply_op(op_type, a, name): # pragma: no cover
    if not all(isinstance(x, bool) for x in a): # pragma: no cover
        raise TypeError('Expected bool for argument \"a\" not ' + str(a[0]) + '.') # pragma: no cover
    attr = {'a': {'list': {'b': a}}} # pragma: no cover
    return MockOperation(name, op_type, attr) # pragma: no cover
op_def_library = type('MockOpDefLib', (object,), {})() # pragma: no cover
op_def_library.apply_op = mock_apply_op # pragma: no cover
_l_ = lambda x: print(f'Line executed: {x}') # pragma: no cover
class MockSelf: # pragma: no cover
    def assertProtoEquals(self, expected, actual): # pragma: no cover
        expected = expected.replace('\n', '').replace(' ', '').strip() # pragma: no cover
        actual = f"name:'{actual.name}'op:'{actual.op}'attr{{key:'a'value{{list{{b:{'b:'.join([str(b).lower() for b in actual.attr['a']['list']['b']])}}}}}}}" # pragma: no cover
        assert expected == actual.strip(), f"Expected: {expected}, Actual: {actual}" # pragma: no cover
    def assertRaises(self, exc_type): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __init__(self, exc_type): # pragma: no cover
                self.exc_type = exc_type # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                return self.exc_type is not None and issubclass(exc_type, self.exc_type) # pragma: no cover
        return ContextManager(exc_type) # pragma: no cover
    def assertEqual(self, x, y): # pragma: no cover
        assert x == y, f"Expected: {x}, Actual: {y}" # pragma: no cover
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
