import numpy as np # pragma: no cover

options = type('Mock', (object,), {})() # pragma: no cover
def create_tensor_data(dtype, shape, min_value, max_value): # pragma: no cover
    return np.random.uniform(low=min_value, high=max_value, size=shape).astype(dtype) # pragma: no cover
def make_zip_of_tests(options, test_parameters, build_graph, build_inputs): # pragma: no cover
    for param_combination in test_parameters: # pragma: no cover
        for input_shape in param_combination['input_shape']: # pragma: no cover
            for depth_radius in param_combination['depth_radius']: # pragma: no cover
                for bias in param_combination['bias']: # pragma: no cover
                    for alpha in param_combination['alpha']: # pragma: no cover
                        for beta in param_combination['beta']: # pragma: no cover
                            parameters = { # pragma: no cover
                                'input_shape': input_shape, # pragma: no cover
                                'depth_radius': depth_radius, # pragma: no cover
                                'bias': bias, # pragma: no cover
                                'alpha': alpha, # pragma: no cover
                                'beta': beta # pragma: no cover
                            } # pragma: no cover
                            inputs, outputs = build_graph(parameters) # pragma: no cover
                            with tf.compat.v1.Session() as sess: # pragma: no cover
                                build_inputs(parameters, sess, inputs, outputs) # pragma: no cover

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
