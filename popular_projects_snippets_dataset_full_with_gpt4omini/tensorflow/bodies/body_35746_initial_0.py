import numpy as np # pragma: no cover

def line_template(x): return tf.linalg.matmul(x, np.array([[1.0], [2.0]])) # pragma: no cover
test_input = np.array([[1.0], [2.0], [3.0]]) # pragma: no cover
test_output = np.array([[5.0], [11.0], [17.0]]) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
from l3.Runtime import _l_
test_prediction = line_template(test_input)
_l_(8787)
aux = math_ops.reduce_mean(
    math_ops.square(test_prediction - test_output))
_l_(8788)
exit(aux)
