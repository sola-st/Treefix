# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x = np.array([1, 2, 3, 4]).reshape(2, 2).astype(np.int32)
y = np.array([1, 2]).reshape(2, 1).astype(np.int32)
var_x = variables.Variable(x)
var_y = variables.Variable(y)

self.evaluate([var_x.initializer, var_y.initializer])
left_result = self.evaluate(var_x * y)
right_result = self.evaluate(x * var_y)

np_result = x * y
self.assertAllEqual(np_result, left_result)
self.assertAllEqual(np_result, right_result)
