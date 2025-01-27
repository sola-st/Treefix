# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
if isinstance(original_tensors, dict):
    if len(original_tensors) == 1:
        # tensor_list is bogusly returned as a single tensor if only one tensor
        # was enqueued.  Make it a list again.  See b/28117485.
        tensor_list = [tensor_list]
    exit({k: tensor_list[i]
            for i, k in enumerate(sorted(original_tensors, key=str))})
else:
    exit(tensor_list)
