import numpy as np # pragma: no cover

use_tensor_inputs = True # pragma: no cover
ops = type('Mock', (object,), {'convert_to_tensor': staticmethod(lambda x: tf.convert_to_tensor(x))})() # pragma: no cover
offset_height = 10 # pragma: no cover
offset_width = 20 # pragma: no cover
target_height = 50 # pragma: no cover
target_width = 100 # pragma: no cover
x = np.random.rand(256, 256, 3) # pragma: no cover
image_ops = type('Mock', (object,), {'crop_to_bounding_box': staticmethod(lambda img, offset_h, offset_w, target_h, target_w: img[offset_h:offset_h + target_h, offset_w:offset_w + target_w])})() # pragma: no cover
self = type('Mock', (object,), {'cached_session': lambda: (lambda: None), 'evaluate': staticmethod(lambda x: x)})() # pragma: no cover

import numpy as np # pragma: no cover

use_tensor_inputs = True # pragma: no cover
ops = type('Mock', (), {'convert_to_tensor': staticmethod(lambda x: tf.convert_to_tensor(x))})() # pragma: no cover
offset_height = 10 # pragma: no cover
offset_width = 20 # pragma: no cover
target_height = 50 # pragma: no cover
target_width = 100 # pragma: no cover
self = type('Mock', (), {'cached_session': lambda: tf.compat.v1.Session(), 'evaluate': lambda x: x.eval()})() # pragma: no cover

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
