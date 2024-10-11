# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_safety_test.py
small_mapping = {
    "tf.contrib.layers.poincare_normalize":
        "tfa.layers.PoincareNormalize",
    "tf.contrib.layers.maxout":
        "tfa.layers.Maxout",
    "tf.contrib.layers.group_norm":
        "tfa.layers.GroupNormalization",
    "tf.contrib.layers.instance_norm":
        "tfa.layers.InstanceNormalization",
}
for symbol, replacement in small_mapping.items():
    text = "{}('stuff', *args, **kwargs)".format(symbol)
    _, report, _, _ = self._upgrade(text)
    self.assertIn(replacement, report)
