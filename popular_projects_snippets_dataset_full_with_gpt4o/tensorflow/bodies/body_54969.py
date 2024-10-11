# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/versions_test.py
self.assertEqual(type(versions.__version__), str)
self.assertEqual(type(versions.VERSION), str)
# This pattern will need to grow as we include alpha, builds, etc.
self.assertRegex(versions.__version__, r'^\d+\.\d+\.(\d+(\-\w+)?|head)$')
self.assertRegex(versions.VERSION, r'^\d+\.\d+\.(\d+(\-\w+)?|head)$')
