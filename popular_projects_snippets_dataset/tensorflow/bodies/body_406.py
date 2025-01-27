# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.io.decode_raw(bytes=[1,2,3], output_dtype=tf.int32)"
expected_text = (
    "tf.io.decode_raw(input_bytes=[1,2,3], output_dtype=tf.int32)")
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
