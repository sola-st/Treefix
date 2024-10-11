import numpy as np # pragma: no cover

images = np.random.rand(10, 64, 64, 3).astype(np.float32) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
from l3.Runtime import _l_
aux = array_ops.reverse_v2(images, [1, 2])
_l_(21648)
exit(aux)
