# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/module_test.py
self.assertIn('TensorFlow', tf.__doc__)
self.assertNotIn('Wrapper', tf.__doc__)
