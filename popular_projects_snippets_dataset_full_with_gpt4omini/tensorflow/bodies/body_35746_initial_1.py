import numpy as np # pragma: no cover

line_template = lambda x: tf.keras.Sequential([tf.keras.layers.Dense(1)])(x) # pragma: no cover
test_input = np.array([[1], [2], [3]], dtype=np.float32) # pragma: no cover
test_output = np.array([[2], [4], [6]], dtype=np.float32) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/template_test.py
from l3.Runtime import _l_
test_prediction = line_template(test_input)
_l_(8787)
aux = math_ops.reduce_mean(
    math_ops.square(test_prediction - test_output))
_l_(8788)
exit(aux)
