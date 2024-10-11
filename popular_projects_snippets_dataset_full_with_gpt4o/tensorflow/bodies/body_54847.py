# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
value = TwoTensors([1, 2, 3], [1.0, 2.0], "red")
spec = TwoTensorsSpec.from_value(value)
tensor_list = spec._to_tensor_list(value)
self.assertLen(tensor_list, 2)
self.assertIs(tensor_list[0], value.x)
self.assertIs(tensor_list[1], value.y)
