# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
tensor_proto.half_val.extend(
    [ExtractBitsFromFloat16(x) for x in proto_values])
