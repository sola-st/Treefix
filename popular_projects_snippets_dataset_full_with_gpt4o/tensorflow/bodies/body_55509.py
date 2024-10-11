# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
tensor_proto.dcomplex_val.extend(
    [v.item() for x in proto_values for v in [x.real, x.imag]])
