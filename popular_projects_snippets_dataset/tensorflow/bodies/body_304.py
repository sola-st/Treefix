# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = (
    "tf.random.multinomial(logits, samples, seed, name, output_dtype)\n"
    )
_, unused_report, unused_errors, new_text = self._upgrade(text)
expected_text = (
    "tf.random.categorical(logits=logits, num_samples=samples, seed=seed, "
    "name=name, dtype=output_dtype)\n"
    )
self.assertEqual(new_text, expected_text)

text = (
    "tf.multinomial(logits, samples, seed, name, output_dtype)\n"
    )
_, unused_report, unused_errors, new_text = self._upgrade(text)
expected_text = (
    "tf.random.categorical(logits=logits, num_samples=samples, seed=seed, "
    "name=name, dtype=output_dtype)\n"
    )
self.assertEqual(new_text, expected_text)
