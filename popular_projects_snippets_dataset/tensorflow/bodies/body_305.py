# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text1 = "tf.random_poisson(lam, shape, dtype)"
text2 = "tf.random.poisson(lam, shape, dtype)"
expected_text = "tf.random.poisson(lam=lam, shape=shape, dtype=dtype)"
_, unused_report, unused_errors, new_text1 = self._upgrade(text1)
self.assertEqual(new_text1, expected_text)
_, unused_report, unused_errors, new_text2 = self._upgrade(text2)
self.assertEqual(new_text2, expected_text)
