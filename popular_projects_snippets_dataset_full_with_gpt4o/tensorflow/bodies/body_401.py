# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.nn.erosion2d(v, k, s, r, p)"
expected_text = "tf.nn.erosion2d(v, k, s, r, p, data_format='NHWC')"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
