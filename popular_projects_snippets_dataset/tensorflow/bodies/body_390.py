# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.saved_model.load(sess, ['foo_graph'])"
expected = "tf.compat.v1.saved_model.load(sess, ['foo_graph'])"
_, report, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
expected_info = "tf.saved_model.load works differently in 2.0"
self.assertIn(expected_info, report)
