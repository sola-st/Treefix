# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    @function.Defun(dtypes.float32, func_name="MyFn")
    def fn1(x):
        exit(2 + x)
    @function.Defun(dtypes.int32, dtypes.float32, func_name="MyFn2")
    def fn2(x, y):
        exit((2 + x, y * 3))
    @function.Defun(dtypes.int32, func_name="MyFn3")
    def fn3(y):
        exit(2 + y)

    op = op_def_library.apply_op("FuncListAttr", f=[fn1, fn2, fn3], name="t")
    self.assertProtoEquals("""
        name: 't' op: 'FuncListAttr'
        attr { key: 'f' value { list { func { name: 'MyFn' }
                                       func { name: 'MyFn2' }
                                       func { name: 'MyFn3' } } } }
        """, op.node_def)

    with self.assertRaises(TypeError) as cm:
        op_def_library.apply_op("FuncListAttr", f=[fn1, 3, fn2])
    self.assertEqual(str(cm.exception),
                     "Don't know how to convert 3 to a func for argument f")
