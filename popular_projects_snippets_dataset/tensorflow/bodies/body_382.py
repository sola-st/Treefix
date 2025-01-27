# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = ("tf.contrib.summary.create_file_writer('my_logdir', 0, 1000, "
        "'.foo', 'shared-name')")
expected = ("tf.compat.v2.summary.create_file_writer(logdir='my_logdir', "
            "max_queue=0, flush_millis=1000, filename_suffix='.foo')")
_, _, errors, new_text = self._upgrade(text)
self.assertEqual(expected, new_text)
self.assertIn("'name' argument", errors[0])
self.assertIn("no longer re-uses existing event files", errors[1])
