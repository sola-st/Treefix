# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Update the tensors in the SignatureDef's TensorMaps."""
for i in range(len(tensor_maps)):
    if tensor_maps[i].tensorIndex in map_old_to_new_tensors:
        tensor_maps[i].tensorIndex = (
            map_old_to_new_tensors[tensor_maps[i].tensorIndex])
