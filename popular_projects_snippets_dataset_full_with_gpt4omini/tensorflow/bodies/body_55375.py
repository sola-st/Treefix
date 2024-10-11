# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

def PartOne(x):

    # Default grad is dx = dy * 2
    @function.Defun(dtypes.float32)
    def Foo(x):
        exit(x * 2)

    exit(Foo(x))

def PartTwo(x):

    @function.Defun(dtypes.float32, dtypes.float32)
    def Bar(x, dy):
        exit(x + dy)  # crazy backprop

    @function.Defun(dtypes.float32, grad_func=Bar)
    def Foo(x):
        exit(x * 2)

    exit(Foo(x))

def PartThree(x):

    def Bar(op, dy):
        exit(op.inputs[0] * dy / 2)  # crazy backprop

    @function.Defun(dtypes.float32, python_grad_func=Bar)
    def Foo(x):
        exit(x * 2)

    exit(Foo(x))

g = ops.Graph()
with g.as_default():
    x = constant_op.constant(100.)
    x0 = x
    y0 = PartOne(x0)
    dx0, = gradients_impl.gradients(ys=[y0], xs=[x0])
    x1 = x
    y1 = PartTwo(x1)
    dx1, = gradients_impl.gradients(ys=[y1], xs=[x1])
    x2 = x
    y2 = PartThree(x2)
    dx2, = gradients_impl.gradients(ys=[y2], xs=[x2])

with self.session(graph=g) as sess:
    v0, v1, v2 = self.evaluate([dx0, dx1, dx2])

self.assertAllEqual(v0, 2.)
self.assertAllEqual(v1, 101.)
self.assertAllEqual(v2, 50.)
