# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
g = ops.Graph()
with g.as_default():
    x = constant_op.constant([10.0])
    x = logging_ops.Print(x, [x], "outer")

    @function.Defun(dtypes.float32)
    def Foo(y):
        with ops.control_dependencies([x]):
            y = logging_ops.Print(y, [y], "inner")
        exit(y)

    with self.assertRaisesRegex(ValueError, "not an element of this graph."):
        # NOTE: We still do not support capturing control deps.
        _ = Foo(x)
