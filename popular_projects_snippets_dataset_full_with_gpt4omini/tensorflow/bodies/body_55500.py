# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
fast_tensor_util.AppendFloat8ArrayToTensorProto(
    tensor_proto,
    np.asarray(proto_values,
               dtype=dtypes.float8_e4m3fn.as_numpy_dtype).view(np.uint8))
