# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.contrib.distribute.CrossDeviceOps()"
expected = "tf.distribute.CrossDeviceOps()"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)

text = "tf.contrib.distribute.MirroredStrategy"
expected = "tf.contrib.distribute.MirroredStrategy"
_, _, errors, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
self.assertIn("migrated to tf.distribute.MirroredStrategy", errors[0])

text = "tf.distribute.MirroredStrategy"
expected = "tf.distribute.MirroredStrategy"
_, report, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
self.assertIn("tf.distribute.MirroredStrategy API has changed", report)
self.assertIn("make_dataset_iterator->experimental_distribute_dataset",
              report)

text = "tf.contrib.distribute.TPUStrategy"
expected = "tf.contrib.distribute.TPUStrategy"
_, _, errors, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
self.assertIn("migrated to tf.distribute.TPUStrategy",
              errors[0])

text = "tf.contrib.distribute.foo"
expected = "tf.contrib.distribute.foo"
_, report, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
self.assertIn("tf.contrib.distribute.* have been migrated", report)
