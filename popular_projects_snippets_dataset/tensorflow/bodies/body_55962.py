# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op("AttrEnum", a="oranges", name="e")
    self.assertProtoEquals("""
        name: 'e' op: 'AttrEnum' attr { key: 'a' value { s: 'oranges' } }
        """, op.node_def)

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op("AttrEnum", a="invalid")
    self.assertEqual(str(cm.exception),
                     'Attr \'a\' of \'AttrEnum\' Op '
                     'passed string \'invalid\' not in: '
                     '"apples", "oranges".')
