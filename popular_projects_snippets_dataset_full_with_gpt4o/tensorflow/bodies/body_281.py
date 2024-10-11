# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for contrib_alias in ["tf.contrib.", "contrib_"]:
    text = contrib_alias + "layers.xavier_initializer()\n"
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(
        new_text,
        "tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, "
        "mode=\"fan_avg\", "
        "distribution=\"uniform\")\n",
    )

    text = "slim.xavier_initializer(True or False)\n"
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(
        new_text,
        "tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, "
        "mode=\"fan_avg\", "
        "distribution=(\"uniform\" if True or False else "
        "\"truncated_normal\"))\n",
    )

    text = "slim.xavier_initializer(uniform=(True or False))\n"
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(
        new_text,
        "tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, "
        "mode=\"fan_avg\", "
        "distribution=(\"uniform\" if True or False else "
        "\"truncated_normal\"))\n",
    )

    text = contrib_alias + "layers.xavier_initializer_conv2d(False, 12)\n"
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(
        new_text,
        "tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, "
        "mode=\"fan_avg\", "
        "distribution=(\"uniform\" if False else \"truncated_normal\"), "
        "seed=12)\n",
    )

    text = (contrib_alias + "layers.xavier_initializer_conv2d("
            "False, 12, tf.float32)\n")
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(
        new_text,
        "tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, "
        "mode=\"fan_avg\", "
        "distribution=(\"uniform\" if False else \"truncated_normal\"), "
        "seed=12, "
        "dtype=tf.float32)\n",
    )

    text = (contrib_alias + "layers.xavier_initializer("
            "False, 12, dtypes=tf.float32)\n")
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(
        new_text,
        "tf.compat.v1.keras.initializers.VarianceScaling(scale=1.0, "
        "mode=\"fan_avg\", "
        "distribution=(\"uniform\" if False else \"truncated_normal\"), "
        "seed=12, "
        "dtypes=tf.float32)\n",
    )
