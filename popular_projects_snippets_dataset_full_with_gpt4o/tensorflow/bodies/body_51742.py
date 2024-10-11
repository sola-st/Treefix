# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
expected = array_ops.placeholder(dtypes.float32, 1, name="x")
tensor_info = utils.build_tensor_info(expected)
tensor_info.name = "blah:0"  # Nonexistent name.
with self.assertRaises(KeyError):
    utils.get_tensor_from_tensor_info(tensor_info)
tensor_info.ClearField("name")  # Malformed (missing encoding).
with self.assertRaises(ValueError):
    utils.get_tensor_from_tensor_info(tensor_info)
