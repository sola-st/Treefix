# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/sysconfig_test.py
build_info = sysconfig_lib.get_build_info()
self.assertIsInstance(build_info, dict)
