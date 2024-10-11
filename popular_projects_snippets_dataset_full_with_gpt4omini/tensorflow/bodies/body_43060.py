# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
with self.assertRaises(tf_export.InvalidSymbolNameError):
    tf_export.tf_export('valid', v1=['estimator.invalid'])
