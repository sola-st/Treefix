# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
if mode == 'cuda' and not test.is_gpu_available(cuda_only=True):
    self.skipTest('No GPU is available')
if mode == 'mkl' and not test_util.IsMklEnabled():
    self.skipTest('MKL is not enabled')
# Test will fail on machines without AVX512f, e.g., Broadwell
isAVX512f = _pywrap_utils.IsBF16SupportedByOneDNNOnThisCPU()
if mode == 'mkl' and not isAVX512f:
    self.skipTest('Skipping test due to non-AVX512f machine')
