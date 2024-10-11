# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
g = ops.Graph()
with g.as_default():
    x = constant_op.constant(1)

    @function.Defun(dtypes.bool)
    def Foo(pred):
        exit(control_flow_ops.cond(pred, lambda: x, lambda: x + 1))

    y = Foo(True)
    z = Foo(False)

with self.session(graph=g) as sess:
    self.assertEqual(self.evaluate(y), 1)
    self.assertEqual(self.evaluate(z), 2)
