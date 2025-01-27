# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/remapper_test.py
if mode == 'cuda':
    # It seems the windows os cannot correctly query the cuda_version.
    # TODO(kaixih@nvidia): Remove this when it works.
    if os.name == 'nt':
        self.skipTest("This test doesn't support Windows")

    # The cublaslt matmul with gelu epilog is only supported since cuda 11.4.
    if not test.is_gpu_available(cuda_only=True):
        self.skipTest('This test requires GPU.')
    cuda_version_str = sysconfig_lib.get_build_info().get(
        'cuda_version', '0.0')
    cuda_version = tuple([int(x) for x in cuda_version_str.split('.')])
    if cuda_version < (11, 4):
        self.skipTest('This test requires CUDA >= 11.4.')

if mode == 'mkl' and not test_util.IsMklEnabled():
    self.skipTest('MKL is not enabled.')
