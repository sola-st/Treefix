import numpy as np # pragma: no cover

class MockFastTensorUtil:# pragma: no cover
    def AppendFloat16ArrayToTensorProto(self, tensor_proto, values):# pragma: no cover
        pass# pragma: no cover
fast_tensor_util = MockFastTensorUtil() # pragma: no cover
tensor_proto = object() # pragma: no cover
proto_values = [1.0, 2.0, 3.0] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
# TODO: Remove the conversion if cython supports np.float16_t
from l3.Runtime import _l_
fast_tensor_util.AppendFloat16ArrayToTensorProto(
    tensor_proto,
    np.asarray(proto_values, dtype=np.float16).view(np.uint16))
_l_(18273)
