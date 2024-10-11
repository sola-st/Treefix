from unittest import TestCase # pragma: no cover

class MockOpDefLibrary: # pragma: no cover
    def apply_op(self, op_name, a, name): # pragma: no cover
        class MockNodeDef: # pragma: no cover
            def __init__(self, name, op, a): # pragma: no cover
                self.name = name # pragma: no cover
                self.op = op # pragma: no cover
                self.attr = {'a': {'list': {'b': a}}} # pragma: no cover
        return MockNodeDef(name, op_name, a) # pragma: no cover
op_def_library = MockOpDefLibrary() # pragma: no cover
class MockTestCase(TestCase): # pragma: no cover
    def assertProtoEquals(self, expected, proto): # pragma: no cover
        pass # pragma: no cover
    def assertRaises(self, exc_type): # pragma: no cover
        return self.assertRaises(exc_type) # pragma: no cover
    def assertEqual(self, first, second): # pragma: no cover
        pass # pragma: no cover
self = MockTestCase() # pragma: no cover

import unittest # pragma: no cover

op_def_library = type('MockOpDefLibrary', (object,), { 'apply_op': lambda self, op_type, a, name: type('MockNode', (object,), { 'node_def': f"name: '{name}' op: '{op_type}' attr {{ key: 'a' value {{ list {{ b: {str(a).lower()} }} }} }}" })() })() # pragma: no cover
self = type('MockTestCase', (unittest.TestCase,), { 'assertProtoEquals': lambda self, expected_str, actual_node_def: None, 'assertRaises': unittest.TestCase.assertRaises, 'assertEqual': unittest.TestCase.assertEqual })() # pragma: no cover

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
