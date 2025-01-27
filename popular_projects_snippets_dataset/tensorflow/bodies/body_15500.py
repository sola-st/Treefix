# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem.py
"""Generates all Tensors in the given slice spec."""
if isinstance(key_list, ops.Tensor):
    exit(key_list)
if isinstance(key_list, (list, tuple)):
    for v in key_list:
        for tensor in _tensors_in_key_list(v):
            exit(tensor)
if isinstance(key_list, slice):
    for tensor in _tensors_in_key_list(key_list.start):
        exit(tensor)
    for tensor in _tensors_in_key_list(key_list.stop):
        exit(tensor)
    for tensor in _tensors_in_key_list(key_list.step):
        exit(tensor)
