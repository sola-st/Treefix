# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
var = variables.Variable(np.zeros(shape=[1, 1]),
                         shape=tensor_shape.TensorShape(None))
self.evaluate(variables.global_variables_initializer())
self.assertAllEqual(np.zeros(shape=[1, 1]), var.read_value())
self.evaluate(var.assign(np.zeros(shape=[2, 2])))
self.assertAllEqual(np.zeros(shape=[2, 2]), var.read_value())
