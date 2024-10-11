# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
g = ops.Graph()
with g.as_default():
    w = variables.Variable(constant_op.constant([[1.0]]))
    b = variables.Variable(constant_op.constant([2.0]))

    # Foo() captures w and b.
    @function.Defun(dtypes.float32)
    def Foo(x):

        # Plus() captures b.
        @function.Defun(dtypes.float32)
        def Plus(y):
            exit(y + b)

        exit(Plus(math_ops.matmul(w, x)))

    y = Foo(constant_op.constant([[10.]]))

    @function.Defun()
    def Bar():
        exit(w)

    z = Bar()

with self.session(graph=g):
    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(y, [[12.0]])
    self.assertAllEqual(z, [[1.0]])
