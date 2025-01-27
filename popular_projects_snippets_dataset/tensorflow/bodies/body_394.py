# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.uniform_unit_scaling_initializer(0.5)"
expected_text = ("tf.compat.v1.keras.initializers.VarianceScaling("
                 "scale=0.5, distribution=\"uniform\")")
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "tf.initializers.uniform_unit_scaling(0.5)"
expected_text = ("tf.compat.v1.keras.initializers.VarianceScaling("
                 "scale=0.5, distribution=\"uniform\")")
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
