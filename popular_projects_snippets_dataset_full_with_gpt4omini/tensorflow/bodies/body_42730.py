# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
l = [[1, 2], [3, 4]]
t = _create_tensor(l)
for list_element, tensor_element in zip(l, t):
    self.assertAllEqual(list_element, tensor_element.numpy())
