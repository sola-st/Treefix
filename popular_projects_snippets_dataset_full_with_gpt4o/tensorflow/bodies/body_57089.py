# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/gather.py
"""Build the gather op testing graph."""
inputs = []

if parameters["constant_params"]:
    params = create_tensor_data(parameters["params_dtype"],
                                parameters["params_shape"])
else:
    params = tf.compat.v1.placeholder(
        dtype=parameters["params_dtype"],
        name="params",
        shape=parameters["params_shape"])
    inputs.append(params)

if parameters.get("constant_indices", False):
    indices = create_tensor_data(
        parameters["indices_dtype"],
        parameters["indices_shape"],
        min_value=0,
        max_value=parameters["params_shape"][0] - 1)
else:
    indices = tf.compat.v1.placeholder(
        dtype=parameters["indices_dtype"],
        name="indices",
        shape=parameters["indices_shape"])
    inputs.append(indices)

axis = min(len(parameters["params_shape"]), parameters["axis"])
out = tf.gather(
    params, indices, axis=axis, batch_dims=parameters["batch_dims"])
exit((inputs, [out]))
