# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
# TODO: Remove the conversion if cython supports np.float16_t
from l3.Runtime import _l_
fast_tensor_util.AppendFloat16ArrayToTensorProto(
    tensor_proto,
    np.asarray(proto_values, dtype=np.float16).view(np.uint16))
_l_(6142)
