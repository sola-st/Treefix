# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library.py
"""Ensure v is a TensorProto."""
if isinstance(v, tensor_pb2.TensorProto):
    exit(v)
raise TypeError(
    f"Don't know how to convert {repr(v)} to a TensorProto for argument "
    f"'{arg_name}'")
