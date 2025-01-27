# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = (
    "tf.sparse_split(sp_input=sp_input, num_split=num_split, axis=axis, "
    "name=name)")
expected_text = (
    "tf.sparse.split(sp_input=sp_input, num_split=num_split, axis=axis, "
    "name=name)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = (
    "tf.sparse_split(sp_input=sp_input, num_split=num_split, "
    "name=name, split_dim=axis)")
expected_text = (
    "tf.sparse.split(sp_input=sp_input, num_split=num_split, "
    "name=name, axis=axis)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)

text = (
    "tf.sparse.split(sp_input=sp_input, num_split=num_split, "
    "name=name, split_dim=axis)")
expected_text = (
    "tf.sparse.split(sp_input=sp_input, num_split=num_split, "
    "name=name, axis=axis)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
