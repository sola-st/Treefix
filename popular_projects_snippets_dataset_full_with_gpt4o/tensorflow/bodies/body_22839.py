# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
endpoints = original_def.inputs if is_input else original_def.outputs
converted_endpoints = (
    converted_def.inputs if is_input else converted_def.outputs)
self.assertEqual(set(endpoints.keys()), set(converted_endpoints.keys()))
for key in endpoints:
    original_input = endpoints[key]
    converted_input = converted_endpoints[key]
    self.assertEqual(original_input.name, converted_input.name)
    self.assertEqual(original_input.dtype, converted_input.dtype)
    self.assertEqual(
        tensor_shape.TensorShape(original_input.tensor_shape).as_list(),
        tensor_shape.TensorShape(converted_input.tensor_shape).as_list())
