# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for contrib_alias in ["tf.contrib.", "contrib_"]:
    _, report, _, _ = self._upgrade(contrib_alias + "layers.layer_norm")
    self.assertIn(
        "`tf.contrib.layers.layer_norm` has been deprecated", report)
