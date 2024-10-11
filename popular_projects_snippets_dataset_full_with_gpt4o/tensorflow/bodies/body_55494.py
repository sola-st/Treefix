# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
fast_tensor_util.AppendBFloat16ArrayToTensorProto(
    tensor_proto, np.asarray(
        proto_values, dtype=dtypes.bfloat16.as_numpy_dtype).view(np.uint16))
