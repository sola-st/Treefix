import numpy as np # pragma: no cover

use_tensor_inputs = True # pragma: no cover
offset_height = 10 # pragma: no cover
offset_width = 10 # pragma: no cover
target_height = 64 # pragma: no cover
target_width = 64 # pragma: no cover
x = np.random.rand(128, 128, 3).astype(np.float32) # pragma: no cover
self = type('MockSelf', (object,), {'cached_session': lambda s: tf.compat.v1.Session().__enter__, 'evaluate': lambda s, y: y})() # pragma: no cover

use_tensor_inputs = True # pragma: no cover
offset_height = 10 # pragma: no cover
offset_width = 15 # pragma: no cover
target_height = 100 # pragma: no cover
target_width = 100 # pragma: no cover
self = type('Mock', (object,), {'cached_session': lambda s: type('MockSession', (object,), {'__enter__': lambda s: tf.compat.v1.Session(), '__exit__': lambda s, exc_type, exc_val, exc_tb: None})(), 'evaluate': lambda s, y: tf.Session().run(y)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
from l3.Runtime import _l_
if use_tensor_inputs:
    _l_(21149)

    offset_height = ops.convert_to_tensor(offset_height)
    _l_(21143)
    offset_width = ops.convert_to_tensor(offset_width)
    _l_(21144)
    target_height = ops.convert_to_tensor(target_height)
    _l_(21145)
    target_width = ops.convert_to_tensor(target_width)
    _l_(21146)
    x_tensor = ops.convert_to_tensor(x)
    _l_(21147)
else:
    x_tensor = x
    _l_(21148)

y = image_ops.crop_to_bounding_box(x_tensor, offset_height, offset_width,
                                   target_height, target_width)
_l_(21150)

with self.cached_session():
    _l_(21152)

    aux = self.evaluate(y)
    _l_(21151)
    exit(aux)
