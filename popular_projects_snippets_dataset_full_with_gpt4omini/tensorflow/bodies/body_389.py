# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.nn.avg_pool(value=4)"
expected_text = "tf.nn.avg_pool2d(input=4)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
