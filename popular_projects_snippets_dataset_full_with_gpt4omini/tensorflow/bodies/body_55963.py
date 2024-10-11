# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    op = op_def_library.apply_op(
        "AttrEnumList", a=["oranges", "apples"], name="f")
    self.assertProtoEquals("""
        name: 'f' op: 'AttrEnumList'
        attr { key: 'a' value { list { s: 'oranges' s: 'apples' } } }
        """, op.node_def)

    with self.assertRaises(ValueError) as cm:
        op_def_library.apply_op(
            "AttrEnumList", a=["apples", "invalid", "oranges"])
    self.assertEqual(str(cm.exception),
                     'Attr \'a\' of \'AttrEnumList\' Op '
                     'passed string \'invalid\' not '
                     'in: "apples", "oranges".')
