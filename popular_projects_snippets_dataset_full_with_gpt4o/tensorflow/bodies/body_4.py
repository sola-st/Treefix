# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/module_test.py
# Check that a few modules are in __dict__.
# pylint: disable=pointless-statement
tf.nn
tf.keras
tf.image
# pylint: enable=pointless-statement
self.assertIn('nn', tf.__dict__)
self.assertIn('keras', tf.__dict__)
self.assertIn('image', tf.__dict__)
