array_ops = type('Mock', (object,), {'Const': staticmethod(lambda value, dtype: tf.constant(value, dtype=dtype))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/examples/customization/ops_defs.py
from l3.Runtime import _l_
ret = array_ops.Const(value=100.0, dtype=dtypes.float32)
_l_(9953)
aux = ret
_l_(9954)
exit(aux)
