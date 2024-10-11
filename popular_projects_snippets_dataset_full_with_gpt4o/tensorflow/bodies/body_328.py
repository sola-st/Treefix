# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.nn.separable_conv2d(inp, d, pt, strides, pad, rate, name, fmt)"
expected_text = (
    "tf.nn.separable_conv2d(input=inp, depthwise_filter=d, "
    "pointwise_filter=pt, strides=strides, padding=pad, "
    "dilations=rate, name=name, data_format=fmt)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
