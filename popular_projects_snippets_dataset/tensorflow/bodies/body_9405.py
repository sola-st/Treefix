# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/sysconfig_test.py
build_info = sysconfig_lib.get_build_info()
self.assertEqual(build_info["is_rocm_build"], test.is_built_with_rocm())
self.assertEqual(build_info["is_cuda_build"], test.is_built_with_cuda())
