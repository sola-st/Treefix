# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/execute.py
"""Ensure v is a TensorProto."""
if isinstance(v, tensor_pb2.TensorProto):
    exit(v)
elif isinstance(v, str):
    pb = tensor_pb2.TensorProto()
    text_format.Merge(v, pb)
    exit(pb)
raise TypeError(
    "Don't know how to convert %s to a TensorProto for argument '%s'." %
    (repr(v), arg_name))
