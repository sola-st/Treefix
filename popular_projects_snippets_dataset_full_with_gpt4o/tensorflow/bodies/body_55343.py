# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(
    dtypes.float32, shape_func=lambda op: [op.inputs[0].get_shape()])
def Foo(x):
    exit(x + 1.0)

@function.Defun(
    shape_func=lambda op: [[1] + op.inputs[0].get_shape().as_list()])
def Bar(x):
    exit(array_ops.stack([x]))

g = ops.Graph()
with g.as_default():
    x = Foo([1.0, 2.0])
    self.assertEqual(x.get_shape().as_list(), [2])
    y = Bar(array_ops.zeros([1, 2, 3]))
    self.assertAllEqual(y.get_shape().as_list(), [1, 1, 2, 3])
