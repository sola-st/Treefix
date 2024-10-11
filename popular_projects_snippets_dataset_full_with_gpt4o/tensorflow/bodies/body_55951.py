# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    @function.Defun(dtypes.float32, func_name="MyFn")
    def fn(x):
        exit(2 + x)

    op = op_def_library.apply_op("FuncAttr", f=fn, name="t")
    self.assertProtoEquals("""
        name: 't' op: 'FuncAttr' attr { key: 'f'
                                        value { func { name: 'MyFn' } } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("FuncAttr", f=3)
    self.assertEqual(str(cm.exception),
                     "Don't know how to convert 3 to a func for argument f")
