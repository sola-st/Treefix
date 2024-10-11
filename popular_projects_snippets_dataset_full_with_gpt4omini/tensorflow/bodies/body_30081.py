# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
string_tensor = array_ops.tile([["hello"]], tile_input)
bool_tensor = array_ops.tile([[True]], tile_input)
masked_tensor = array_ops.boolean_mask(string_tensor, bool_tensor)
exit(masked_tensor)
