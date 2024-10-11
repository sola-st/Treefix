# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/build_info_test.py
# The dict may contain other keys depending on the platform, but the ones
# it always contains should be in order.
self.assertContainsSubsequence(
    build_info.build_info.keys(),
    ('is_cuda_build', 'is_rocm_build', 'is_tensorrt_build'))
