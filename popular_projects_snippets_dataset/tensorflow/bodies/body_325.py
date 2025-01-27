# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.nn.weighted_moments(x, axes, freq, name, kd)"
expected_text = (
    "tf.nn.weighted_moments(x=x, axes=axes, frequency_weights=freq, "
    "name=name, keepdims=kd)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
