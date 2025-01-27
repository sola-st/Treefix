# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.sparse.concat(ax, inp, name, exp, concat)"
expected_text = (
    "tf.sparse.concat(axis=ax, sp_inputs=inp, name=name, "
    "expand_nonconcat_dims=exp, axis=concat)")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
