import unittest # pragma: no cover

class MockOp:  # A mock class to simulate the operation output # pragma: no cover
    def __init__(self, name, a): # pragma: no cover
        self.node_def = f'name: ''{name}'' op: ''AttrBoolList'' attr {{ key: ''a'' value {{ list {{ ' + ' '.join(['b: ' + str(x).lower() for x in a]) + ' }} }} }}' # pragma: no cover
class MockOpDefLibrary:  # A mock for the op_def_library # pragma: no cover
    def apply_op(self, op_name, a, name): # pragma: no cover
        if any(not isinstance(x, bool) for x in a):  # Ensure `a` only contains bools # pragma: no cover
            raise TypeError(f"Expected bool for argument 'a' not {a}.") # pragma: no cover
        return MockOp(name, a)  # Return a mock operation # pragma: no cover

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
