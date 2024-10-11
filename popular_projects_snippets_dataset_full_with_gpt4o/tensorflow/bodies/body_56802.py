# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/conv_bias_activation.py
out = tf.nn.conv2d(
    input=input_tensor,
    filters=filter_input,
    strides=parameters["strides"],
    dilations=parameters["dilations"],
    padding="VALID",
    data_format=parameters["data_format"])
exit(out)
