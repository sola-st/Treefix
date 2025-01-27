# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_parameter_converter_test.py
attr_specs = {"x": "list(int)", "y": "shape", "z": "float"}
api_info = self.makeApiInfoFromParamSpecs("ConvertAttributes",
                                          ["x", "y", "z"], {}, attr_specs)
tensor_converter = self.makeTensorConverter()

params = [[1, 2.0, np.array(3.0)], [1, 2], 10]
inferred = Convert(api_info, tensor_converter, params)

self.assertEqual(inferred.types, [])
self.assertEqual(inferred.type_lists, [])
self.assertEqual(inferred.lengths, [])
self.assertLen(params, 3)
self.assertEqual(params, [[1, 2, 3], tensor_shape.as_shape([1, 2]), 10.0])
self.assertIsInstance(params[0][0], int)
self.assertIsInstance(params[1], tensor_shape.TensorShape)
self.assertIsInstance(params[2], float)
