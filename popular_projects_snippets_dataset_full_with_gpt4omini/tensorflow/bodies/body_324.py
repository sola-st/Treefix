# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = ("tf.sparse_matmul(a, b, c, d, e, f, g)\n")
expected_text = ("tf.linalg.matmul(a=a, b=b, transpose_a=c, transpose_b=d, "
                 "a_is_sparse=e, b_is_sparse=f, name=g)\n")
_, unused_report, unused_errors, new_text = self._upgrade(text)
self.assertEqual(new_text, expected_text)
