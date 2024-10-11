# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = ("tf.nn.pool(input_a, window_shape_a, pooling_type_a, padding_a, "
        "dilation_rate_a, strides_a, name_a, data_format_a)\n")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text,
                 ("tf.nn.pool(input=input_a, window_shape=window_shape_a,"
                  " pooling_type=pooling_type_a, padding=padding_a, "
                  "dilations=dilation_rate_a, strides=strides_a, "
                  "name=name_a, data_format=data_format_a)\n"))
