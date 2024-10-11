# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
if ns_prefix:
    ns_prefix += "."
for v in values:
    text = "tf." + ns_prefix + v + "(a, b)"
    _, _, _, new_text = self._upgrade(text)
    self.assertEqual("tf.compat.v1." + ns_prefix + v + "(a, b)", new_text)
