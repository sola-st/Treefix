# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.space_to_batch_nd(input, shape, paddings, name)"
expected_text = "tf.space_to_batch(input, shape, paddings, name)"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = "tf.nn.space_to_batch(input, paddings, block_size, name)"
expected_text = (
    "tf.space_to_batch(input=input, paddings=paddings, "
    "block_shape=block_size, name=name)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
