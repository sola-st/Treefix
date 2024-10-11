# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/reduce.py
"""Build the inputs for reduced operators."""

dtype = parameters["input_dtype"]
if boolean_tensor_only:
    dtype = tf.bool
values = [
    create_tensor_data(
        dtype,
        parameters["input_shape"],
        min_value=min_value,
        max_value=max_value)
]
if not parameters["const_axis"]:
    values.append(np.array(parameters["axis"]))
exit((values, sess.run(outputs, feed_dict=dict(zip(inputs, values)))))
