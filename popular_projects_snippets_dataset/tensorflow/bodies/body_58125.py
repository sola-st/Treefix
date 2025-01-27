# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
for i, ti in enumerate(tensor_idxs):
    tensor_idxs[i] = d_old_to_new_tensors.get(ti, -1)
