import numpy as np # pragma: no cover

def create_tensor_data(dtype, shape, min_value, max_value): # pragma: no cover
    return np.random.uniform(min_value, max_value, size=shape).astype(dtype) # pragma: no cover
options = {} # pragma: no cover
test_parameters = [{ # pragma: no cover
    'input_shape': [1, 3, 4, 3], # pragma: no cover
    'depth_radius': 1, # pragma: no cover
    'bias': 0.3, # pragma: no cover
    'alpha': 2, # pragma: no cover
    'beta': 0.25 # pragma: no cover
}] # pragma: no cover
make_zip_of_tests = type('Mock', (object,), {'__call__': lambda self, options, test_parameters, build_graph, build_inputs: None})() # pragma: no cover

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
_l_(8916)

def build_graph(parameters):
    _l_(8920)

    input_tensor = tf.compat.v1.placeholder(
        dtype=tf.float32, name="input", shape=parameters["input_shape"])
    _l_(8917)
    out = tf.nn.local_response_normalization(
        input_tensor,
        depth_radius=parameters["depth_radius"],
        bias=parameters["bias"],
        alpha=parameters["alpha"],
        beta=parameters["beta"])
    _l_(8918)
    aux = ([input_tensor], [out])
    _l_(8919)
    exit(aux)

def build_inputs(parameters, sess, inputs, outputs):
    _l_(8923)

    input_values = create_tensor_data(
        np.float32, parameters["input_shape"], min_value=-4, max_value=10)
    _l_(8921)
    aux = ([input_values], sess.run(
        outputs, feed_dict=dict(zip(inputs, [input_values]))))
    _l_(8922)
    exit(aux)

make_zip_of_tests(options, test_parameters, build_graph, build_inputs)
_l_(8924)
