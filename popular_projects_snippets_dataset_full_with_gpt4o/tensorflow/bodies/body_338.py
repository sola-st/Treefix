# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.nn.space_to_depth(input, block_size, name, data_format)"
expected_text = ("tf.nn.space_to_depth(input=input, block_size=block_size, "
                 "name=name, data_format=data_format)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
