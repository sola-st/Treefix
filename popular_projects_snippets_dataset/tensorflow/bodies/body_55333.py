# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
g = ops.Graph()
with g.as_default():
    x = constant_op.constant(1)

    @function.Defun()
    def Foo():
        exit(control_flow_ops.while_loop(lambda i: i < 10, lambda i: i + x,
                                           [0]))

    y = Foo()

with self.session(graph=g) as sess:
    self.assertEqual(self.evaluate(y), 10)
