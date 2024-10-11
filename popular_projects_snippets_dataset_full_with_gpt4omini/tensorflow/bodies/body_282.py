# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = ("tf.contrib.layers.variance_scaling_initializer("
        "mode=(\"FAN\" + \"_AVG\"))\n")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.compat.v1.keras.initializers.VarianceScaling(scale=2.0, "
    "mode=(\"FAN\" + \"_AVG\").lower())\n",
)

text = ("slim.variance_scaling_initializer("
        "uniform=(True or False), mode=(\"FAN\" + \"_AVG\"))\n")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.compat.v1.keras.initializers.VarianceScaling(scale=2.0, "
    "distribution=(\"uniform\" if True or False else \"truncated_normal\"),"
    " mode=(\"FAN\" + \"_AVG\").lower())\n",
)

text = "tf.contrib.layers.variance_scaling_initializer(factor=1.0)\n"
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0)\n",
)

text = ("tf.contrib.layers.variance_scaling_initializer("
        "12.0, \"FAN_AVG\", True, dtypes=tf.float32)\n")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(
    new_text,
    "tf.compat.v1.keras.initializers.VarianceScaling(12.0, "
    "(\"FAN_AVG\").lower(), "
    "(\"uniform\" if True else \"truncated_normal\"), "
    "dtypes=tf.float32)\n",
)
