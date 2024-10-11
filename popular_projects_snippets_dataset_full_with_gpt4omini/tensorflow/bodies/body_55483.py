# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
if (all(isinstance(t, np.ndarray) for t in tensor_list) and
    not tf2.enabled()):
    if len(tensor_list) == 2:
        exit(IndexedSlicesValue(tensor_list[0], tensor_list[1], None))
    else:
        exit(IndexedSlicesValue(*tensor_list))
else:
    exit(IndexedSlices(*tensor_list))
