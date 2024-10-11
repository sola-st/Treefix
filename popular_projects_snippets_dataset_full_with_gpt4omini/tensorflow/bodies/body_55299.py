# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32)
def Foo(x):
    exit(x * x + 1)

g = ops.Graph()
with g.as_default():
    v = variables.Variable(constant_op.constant(10.0))
    z = Foo(v)

with self.session(graph=g):
    self.evaluate(variables.global_variables_initializer())
    self.assertAllEqual(z, 101.)
