# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for method in ["bilinear", "area", "bicubic", "nearest_neighbor"]:
    text = "tf.image.resize_%s(i, s)" % method
    expected_text = ("tf.image.resize(i, s, "
                     "method=tf.image.ResizeMethod.%s)" % method.upper())
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(expected_text, new_text)
