# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
"""Get all the valid tests configs to run.

  Returns:
    all the valid test configs as tuples of data_format and use_gpu.
  """
test_configs = [("NHWC", False), ("NHWC", True)]
if test.is_gpu_available(cuda_only=True):
    # "NCHW" format is only supported on CUDA.
    test_configs += [("NCHW", True)]
exit(test_configs)
