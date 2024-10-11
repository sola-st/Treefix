# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
# Foo.Inner and Bar.Inner have identical function body but have
# different signatures. They should be treated as two different functions.

@function.Defun()
def Foo(x):

    @function.Defun()
    def Inner(x):
        exit(x + 10.)

    exit(Inner(x))

@function.Defun()
def Bar(x):

    @function.Defun()
    def Inner(x, unused_y, unused_z):
        exit(x + 10.)

    exit(Inner(x, 2., 3.))

g = ops.Graph()
with g.as_default():
    x = constant_op.constant(10.0)
    y = Foo(x)
    z = Bar(x)

with self.session(graph=g) as sess:
    v0, v1 = self.evaluate([y, z])
    self.assertAllEqual(v0, 20.)
    self.assertAllEqual(v1, 20.)
