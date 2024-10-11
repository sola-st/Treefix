import numpy as np # pragma: no cover

create_tensor_data = lambda dtype, shape: tf.random.uniform(shape, dtype=dtype) # pragma: no cover

import numpy as np # pragma: no cover

def create_tensor_data(dtype, shape): return np.random.rand(*shape).astype(dtype) # pragma: no cover
parameters = {"input_dtype": np.float32, "input_shape": (3, 4)} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/arg_min_max.py
from l3.Runtime import _l_
input_value = create_tensor_data(parameters["input_dtype"],
                                 parameters["input_shape"])
_l_(8187)
aux = ([input_value], sess.run(
    outputs, feed_dict=dict(zip(inputs, [input_value]))))
_l_(8188)
exit(aux)
