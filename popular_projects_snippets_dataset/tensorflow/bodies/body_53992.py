# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
a_raw_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = constant_op.constant(a_raw_data)
b = math_ops.add(1, constant_op.constant([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
if ragged_tensors:
    a = ragged_tensor.RaggedTensor.from_tensor(a)
    b = ragged_tensor.RaggedTensor.from_tensor(b)

self.assertAllClose(a, b)
self.assertAllClose(a, a_raw_data)

a_dict = {"key": a}
b_dict = {"key": b}
self.assertAllClose(a_dict, b_dict)

x_list = [a, b]
y_list = [a_raw_data, b]
self.assertAllClose(x_list, y_list)
