# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
scalar_creators = [np.int32, np.int64, np.float32, np.float64]
conversion_functions = [ops.convert_to_tensor, constant_op.constant]

for scalar_creator in scalar_creators:
    for conversion_function in conversion_functions:
        np_val = scalar_creator(3)
        tensor_val = conversion_function(np_val)
        self.assertEqual(tensor_val.numpy().dtype, np_val.dtype)
        self.assertEqual(tensor_val.numpy(), np_val)
