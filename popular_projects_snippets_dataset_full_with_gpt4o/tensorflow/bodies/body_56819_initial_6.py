import numpy as np # pragma: no cover

def create_tensor_data(dtype, shape):# pragma: no cover
    return np.random.rand(*shape).astype(dtype) # pragma: no cover
parameters = {# pragma: no cover
    'input_dtype': np.float32,# pragma: no cover
    'input_shape': (2, 2)# pragma: no cover
} # pragma: no cover
sess = type('Mock', (object,), {'run': lambda self, outputs, feed_dict: np.array([[1.0, 2.0], [3.0, 4.0]])})() # pragma: no cover
outputs = 'mock_output' # pragma: no cover
inputs = ['mock_input'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/arg_min_max.py
from l3.Runtime import _l_
input_value = create_tensor_data(parameters["input_dtype"],
                                 parameters["input_shape"])
_l_(21315)
aux = ([input_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value]))))
_l_(21316)
exit(aux)
