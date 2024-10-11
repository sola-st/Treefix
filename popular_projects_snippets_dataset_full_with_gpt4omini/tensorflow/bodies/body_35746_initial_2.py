import numpy as np # pragma: no cover

math_ops = type('Mock', (object,), {'reduce_mean': staticmethod(np.mean), 'square': staticmethod(np.square)})() # pragma: no cover
line_template = lambda x: 2 * x + 1 # pragma: no cover
test_input = np.array([1, 2, 3, 4, 5]) # pragma: no cover
test_output = np.array([3, 5, 7, 9, 11]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
from l3.Runtime import _l_
test_prediction = line_template(test_input)
_l_(8787)
aux = math_ops.reduce_mean(
    math_ops.square(test_prediction - test_output))
_l_(8788)
exit(aux)
