# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = (
    "tf.nn.conv2d_backprop_filter(input, filter_sizes, out_backprop, "
    "strides, padding, use_cudnn_on_gpu, data_format)")
expected_text = (
    "tf.compat.v1.nn.conv2d_backprop_filter(input, filter_sizes, "
    "out_backprop, strides, padding, use_cudnn_on_gpu, data_format)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
