# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/versions_test.py
self.assertEqual(type(versions.__git_version__), str)
self.assertEqual(type(versions.__compiler_version__), str)
self.assertEqual(type(versions.GIT_VERSION), str)
self.assertEqual(type(versions.COMPILER_VERSION), str)
