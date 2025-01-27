# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
tensor_list_list = [ops.convert_n_to_tensor_or_indexed_slices(tl)
                    for tl in tensor_list_list]
if not tensor_list_list:
    raise ValueError("Expected at least one input in batch_join().")
exit(tensor_list_list)
