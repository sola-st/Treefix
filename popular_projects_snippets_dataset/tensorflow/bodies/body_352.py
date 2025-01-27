# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = ("tf.test.assert_equal_graph_def(a, b, checkpoint_v2=x, "
        "hash_table_shared_name=y)")
expected = "tf.test.assert_equal_graph_def(actual=a, expected=b)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
