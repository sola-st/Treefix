# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = (
    "tf.random.stateless_multinomial(logits, num_samples, seed, "
    "output_dtype=dtype, name=name)")
expected_text = (
    "tf.random.stateless_categorical(logits, num_samples, seed, "
    "dtype=dtype, name=name)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
