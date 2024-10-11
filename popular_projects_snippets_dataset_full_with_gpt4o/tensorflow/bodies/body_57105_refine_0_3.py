import numpy as np # pragma: no cover

make_zip_of_tests = type('Mock', (object,), {})() # pragma: no cover
options = type('Mock', (object,), {})() # pragma: no cover
tf = type('Mock', (object,), {'compat': type('Mock', (object,), {'v1': type('Mock', (object,), {})()})(), 'float32': type('Mock', (object,), {})(), 'nn': type('Mock', (object,), {'local_response_normalization': type('Mock', (object,), {})()})()}) # pragma: no cover
create_tensor_data = lambda dtype, shape, min_value, max_value: np.random.uniform(min_value, max_value, shape).astype(dtype) # pragma: no cover
np = type('Mock', (object,), {'float32': type('Mock', (object,), {})(), 'random': type('Mock', (object,), {'uniform': lambda min_value, max_value, shape: np.random.uniform(min_value, max_value, shape)})()}) # pragma: no cover

import numpy as np # pragma: no cover

def make_zip_of_tests(options, test_parameters, build_graph, build_inputs):# pragma: no cover
    # Mock implementation for testing purposes# pragma: no cover
    for params in test_parameters:# pragma: no cover
        for param_set in zip(*params.values()):# pragma: no cover
            param_dict = dict(zip(params.keys(), param_set))# pragma: no cover
            graph = build_graph(param_dict)# pragma: no cover
            inputs = build_inputs(param_dict, None, None, graph)# pragma: no cover
    return True # pragma: no cover
options = type('Mock', (object,), {})() # pragma: no cover
create_tensor_data = lambda dtype, shape, min_value, max_value: np.random.uniform(min_value, max_value, shape).astype(dtype) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/local_response_norm.py
from l3.Runtime import _l_
"""Make a set of tests to do local_response_norm."""

# Chose a set of parameters
test_parameters = [{
    "input_shape": [[1, 1, 1, 1], [1, 3, 4, 3], [3, 15, 14, 3]],
    "depth_radius": [None, 0, 1, 3, 5],
    "bias": [None, 0.3, -0.1],
    "alpha": [None, 2, -3],
    "beta": [None, 0.25, 2],
}]
_l_(21366)

def build_graph(parameters):
    _l_(21370)

    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    _l_(21367)
    out = tf.nn.local_response_normalization(
        input_tensor,
        depth_radius=parameters["depth_radius"],
        bias=parameters["bias"],
        alpha=parameters["alpha"],
        beta=parameters["beta"])
    _l_(21368)
    aux = ([input_tensor], [out])
    _l_(21369)
    exit(aux)

def build_inputs(parameters, sess, inputs, outputs):
    _l_(21373)

    input_values = create_tensor_data(
        np.float32, parameters["input_shape"], min_value=-4, max_value=10)
    _l_(21371)
    aux = ([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values]))))
    _l_(21372)
    exit(aux)

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
_l_(21374)
