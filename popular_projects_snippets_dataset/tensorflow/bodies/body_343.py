# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
suffix = ".data.experimental.map_and_batch_with_legacy_function(args)"
text = "tf" + suffix
expected = "tf.compat.v1" + suffix
_, unused_report, unused_errors, actual = self._upgrade(text)
self.assertEqual(actual, expected)
