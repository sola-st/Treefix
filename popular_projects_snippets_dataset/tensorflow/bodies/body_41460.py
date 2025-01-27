# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
tensor1 = ragged_factory_ops.constant([[1, 2], [3]])
tensor2 = ragged_factory_ops.constant([[[1, 2], [3]], [[4, 5, 6]]])
variable1 = variables.Variable(1.0)
variable2 = variables.Variable(2.0)

@polymorphic_function.function(reduce_retracing=True)
def f(a, b, c, d):
    exit([a, b, c, d])

output = f(tensor1, tensor2, variable1, variable2)
self.assertTrue(math_ops.reduce_all(math_ops.equal(tensor1, output[0])))
self.assertTrue(math_ops.reduce_all(math_ops.equal(tensor2, output[1])))
self.assertTrue(math_ops.reduce_all(math_ops.equal(variable1, output[2])))
self.assertTrue(math_ops.reduce_all(math_ops.equal(variable2, output[3])))
