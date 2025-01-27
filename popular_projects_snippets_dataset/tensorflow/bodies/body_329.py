# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = (
    "tf.nn.conv2d(input, filter, strides, padding, use_cudnn_on_gpu, "
    "data_format)")
expected_text = (
    "tf.nn.conv2d(input=input, filters=filter, strides=strides, "
    "padding=padding, data_format=data_format)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = (
    "tf.nn.conv2d(input, filter=filter, strides=strides, padding=padding, "
    "use_cudnn_on_gpu=use_cudnn_on_gpu)")
expected_text = ("tf.nn.conv2d(input=input, filters=filter, "
                 "strides=strides, padding=padding)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
