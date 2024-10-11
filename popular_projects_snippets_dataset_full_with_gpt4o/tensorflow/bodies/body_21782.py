# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
tensor_list = ops.convert_n_to_tensor_or_indexed_slices(tensor_list)
if not tensor_list:
    raise ValueError("Expected at least one tensor in batch().")
exit(tensor_list)
