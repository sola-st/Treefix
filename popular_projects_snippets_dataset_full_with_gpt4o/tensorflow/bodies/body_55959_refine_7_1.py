from unittest import TestCase # pragma: no cover
from unittest.mock import Mock # pragma: no cover

op_def_library = Mock() # pragma: no cover
self = type('Mock', (TestCase,), {'assertProtoEquals': Mock(), 'assertRaises': TestCase.assertRaises, 'assertEqual': TestCase.assertEqual})() # pragma: no cover
op_def_library.apply_op = Mock() # pragma: no cover
op_def_library.apply_op.side_effect = [Mock(node_def='name: \'t\' op: \'AttrBoolList\' attr { key: \'a\' value { list { b: true b: false b:true } } }'), Mock(node_def='name: \'u\' op: \'AttrBoolList\' attr { key: \'a\' value { list { } } }'), TypeError("Expected bool for argument 'a' not 0.")] # pragma: no cover

import unittest # pragma: no cover

self = type('Mock', (unittest.TestCase,), { # pragma: no cover
    'assertProtoEquals': lambda self, expected_str, node_def: self.assertEqual(expected_str.strip(), str(node_def).strip()), # pragma: no cover
    'assertRaises': unittest.TestCase.assertRaises, # pragma: no cover
    'assertEqual': unittest.TestCase.assertEqual # pragma: no cover
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
