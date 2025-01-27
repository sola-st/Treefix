# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/build_info_test.py
self.assertEqual(build_info.build_info['is_rocm_build'],
                 test.is_built_with_rocm())
self.assertEqual(build_info.build_info['is_cuda_build'],
                 test.is_built_with_cuda())

# TODO(b/173044576): make the test work for Windows.
if platform.system() != 'Windows':
    # pylint: disable=g-import-not-at-top
    from tensorflow.compiler.tf2tensorrt._pywrap_py_utils import is_tensorrt_enabled
    self.assertEqual(build_info.build_info['is_tensorrt_build'],
                     is_tensorrt_enabled())
