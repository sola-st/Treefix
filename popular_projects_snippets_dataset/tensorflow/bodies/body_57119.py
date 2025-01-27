# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/shape.py
"""Build the shape op testing graph."""
# Note that we intentionally leave out the shape from the input placeholder
# to prevent the Shape operation from being optimized out during conversion.
# TODO(haoliang): Test shape op directly after we have better support for
# dynamic input. Currently we need to introduce a Reshape op to prevent
# shape being constant-folded.
input_value = tf.compat.v1.placeholder(
    dtype=parameters["input_dtype"],
    shape=parameters["input_shape"],
    name="input")
shape_of_new_shape = [len(parameters["new_shape"])]
new_shape = tf.compat.v1.placeholder(
    dtype=tf.int32, shape=shape_of_new_shape, name="new_shape")
reshaped = tf.reshape(input_value, shape=new_shape)
out = tf.shape(input=reshaped, out_type=parameters["out_type"])
exit(([input_value, new_shape], [out]))
