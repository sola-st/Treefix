# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_4/multiplex_4_test.py
result = self._both()
self.assertAllEqual(result,
                    tf.constant([11, 102, 3, 204, 205], dtype=tf.int64))
