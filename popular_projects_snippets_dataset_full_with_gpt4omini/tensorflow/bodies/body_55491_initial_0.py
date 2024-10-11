import numpy as np # pragma: no cover
class Mock: pass # pragma: no cover

fast_tensor_util = type('Mock', (), {'AppendFloat16ArrayToTensorProto': staticmethod(lambda a, b: None)})() # pragma: no cover
tensor_proto = 'mock_tensor_proto' # pragma: no cover
proto_values = [1.0, 2.0, 3.0, 4.0] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
# TODO: Remove the conversion if cython supports np.float16_t
from l3.Runtime import _l_
fast_tensor_util.AppendFloat16ArrayToTensorProto(
    tensor_proto,
    np.asarray(proto_values, dtype=np.float16).view(np.uint16))
_l_(6142)
