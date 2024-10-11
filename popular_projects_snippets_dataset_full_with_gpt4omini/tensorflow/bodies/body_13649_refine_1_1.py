class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover

class Mock: pass # pragma: no cover
class ArrayOps:  # pragma: no cover
    @staticmethod # pragma: no cover
    def broadcast_dynamic_shape(shape_x, shape_y): # pragma: no cover
        return tf.broadcast_static_shape(shape_x, shape_y) # pragma: no cover
    @staticmethod # pragma: no cover
    def shape(tensor): # pragma: no cover
        return tf.shape(tensor) # pragma: no cover
array_ops = ArrayOps() # pragma: no cover
self = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
from l3.Runtime import _l_
aux = array_ops.broadcast_dynamic_shape(
    array_ops.shape(self.loc),
    array_ops.shape(self.scale))
_l_(6085)
exit(aux)
