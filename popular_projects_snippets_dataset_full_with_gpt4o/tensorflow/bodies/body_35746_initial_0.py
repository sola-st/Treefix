import numpy as np # pragma: no cover

line_template = lambda x: np.array([1.2, 2.3, 3.4]) # pragma: no cover
test_input = np.array([1.0, 2.0, 3.0]) # pragma: no cover
test_output = np.array([1.0, 2.0, 3.0]) # pragma: no cover
math_ops = type('Mock', (object,), {'reduce_mean': staticmethod(np.mean), 'square': staticmethod(lambda x: np.square(x))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
from l3.Runtime import _l_
test_prediction = line_template(test_input)
_l_(21178)
aux = math_ops.reduce_mean(
    math_ops.square(test_prediction - test_output))
_l_(21179)
exit(aux)
