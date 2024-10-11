# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
spec = TwoTensorsSpec([5], dtypes.int32, [5, 8], dtypes.float32, "red")
self.assertEqual(spec._flat_tensor_specs,
                 [tensor_spec.TensorSpec([5], dtypes.int32),
                  tensor_spec.TensorSpec([5, 8], dtypes.float32)])
