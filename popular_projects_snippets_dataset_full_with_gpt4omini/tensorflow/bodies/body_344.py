# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
for (name, dtype) in [("int32", "int32"),
                      ("int64", "int64"),
                      ("float", "float32"),
                      ("double", "float64"),
                      ("complex64", "complex64"),
                      ("complex128", "complex128"),
                      ("bfloat16", "bfloat16")]:
    text = "tf.to_%s(x, name='test')" % name
    expected_text = "tf.cast(x, name='test', dtype=tf.%s)" % dtype
    _, unused_report, unused_errors, new_text = self._upgrade(text)
    self.assertEqual(expected_text, new_text)
