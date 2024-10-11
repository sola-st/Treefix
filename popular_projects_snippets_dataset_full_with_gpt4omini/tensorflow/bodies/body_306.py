# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = (
    "tf.nn.convolution(input, filter, padding, strides, dilation_rate, "
    "name, data_format)"
)
_, unused_report, unused_errors, new_text = self._upgrade(text)
expected_text = (
    "tf.nn.convolution(input=input, filters=filter, padding=padding, "
    "strides=strides, dilations=dilation_rate, name=name, "
    "data_format=data_format)"
)
self.assertEqual(new_text, expected_text)
