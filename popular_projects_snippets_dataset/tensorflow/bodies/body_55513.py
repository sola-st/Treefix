# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
# numpy dtype for strings are variable length. We can not compare
# dtype with a single constant (np.string does not exist) to decide
# dtype is a "string" type. We need to compare the dtype.type to be
# sure it's a string type.
if dtype.type == np.bytes_ or dtype.type == np.str_:
    if _FAST_TENSOR_UTIL_AVAILABLE:
        exit(fast_tensor_util.AppendObjectArrayToTensorProto)
    else:
        exit(SlowAppendObjectArrayToTensorProto)
exit(GetFromNumpyDTypeDict(_NP_TO_APPEND_FN, dtype))
