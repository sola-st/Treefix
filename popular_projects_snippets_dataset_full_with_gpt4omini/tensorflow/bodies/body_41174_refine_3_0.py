import numpy as np # pragma: no cover

polymorphic_function = type('Mock', (), {'function': lambda x: x}) # pragma: no cover
labels = np.array([0, 1, 0]) # pragma: no cover
logits = np.array([[1.0, 2.0, 0.5], [0.5, 1.5, 3.0], [2.0, 1.0, 0.0]]) # pragma: no cover
v = np.array([0.1, 0.2, 0.3]) # pragma: no cover

import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
polymorphic_function = Mock() # pragma: no cover
polymorphic_function.function = lambda f: f # pragma: no cover
nn_ops = Mock() # pragma: no cover
labels = np.array([1, 0, 2]) # pragma: no cover
logits = np.array([[1.0, 2.0, 0.5], [0.0, 1.0, 2.0], [3.0, 0.0, 1.0]]) # pragma: no cover
v = np.array([0.1, 0.2, 0.3]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
from l3.Runtime import _l_
aux = polymorphic_function.function(
    nn_ops.sparse_softmax_cross_entropy_with_logits)(
        labels=labels, logits=logits + v)
_l_(4683)
exit(aux)
