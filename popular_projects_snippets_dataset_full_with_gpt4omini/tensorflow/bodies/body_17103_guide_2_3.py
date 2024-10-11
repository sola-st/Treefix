use_tensor_inputs = True # pragma: no cover
offset_height = 10 # pragma: no cover
offset_width = 5 # pragma: no cover
target_height = 50 # pragma: no cover
target_width = 50 # pragma: no cover
self = type('Mock', (), {'cached_session': lambda: tf.compat.v1.Session(), 'evaluate': lambda y: y.eval()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
from l3.Runtime import _l_
if use_tensor_inputs:
    _l_(8738)

    offset_height = ops.convert_to_tensor(offset_height)
    _l_(8732)
    offset_width = ops.convert_to_tensor(offset_width)
    _l_(8733)
    target_height = ops.convert_to_tensor(target_height)
    _l_(8734)
    target_width = ops.convert_to_tensor(target_width)
    _l_(8735)
    x_tensor = ops.convert_to_tensor(x)
    _l_(8736)
else:
    x_tensor = x
    _l_(8737)

y = image_ops.crop_to_bounding_box(x_tensor, offset_height, offset_width,
                                   target_height, target_width)
_l_(8739)

with self.cached_session():
    _l_(8741)

    aux = self.evaluate(y)
    _l_(8740)
    exit(aux)
