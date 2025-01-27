# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_variable.py
with ops.device(dvariable.device):
    exit(api.pack(tensors, layout))
