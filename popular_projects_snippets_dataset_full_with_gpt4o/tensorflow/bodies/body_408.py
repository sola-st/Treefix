# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.framework.load_variable('a')"
expected_text = (
    "tf.train.load_variable('a')")
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
text = "tf.contrib.framework.load_variable(checkpoint_dir='a')"
expected_text = (
    "tf.train.load_variable(ckpt_dir_or_file='a')")
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
