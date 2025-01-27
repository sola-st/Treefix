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
