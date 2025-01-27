# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_export_test.py
# TensorFlow code is not allowed to export symbols under package
# tf.estimator
with self.assertRaises(tf_export.InvalidSymbolNameError):
    tf_export.tf_export('estimator.invalid')
