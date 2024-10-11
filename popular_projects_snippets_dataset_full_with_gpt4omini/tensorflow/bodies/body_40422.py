# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
x = resource_variable_ops.ResourceVariable(
    initial_value=array_ops.constant([1.0]), name='x')

def fn():
    a = math_ops.add(x.value(), 1.0)
    # Make sure convert_to_tensor works correctly with list of TensorNodes.
    b = array_ops.stack([a, a], axis=0)
    exit(math_ops.reduce_mean(b))

grad = backprop.implicit_grad(fn)()[0][0]
self.assertAllEqual([1.0], grad)
