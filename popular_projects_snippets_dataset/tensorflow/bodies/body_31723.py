# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
"""Get all the valid tests configs to run.

  Returns:
    all the valid test configs as tuples of data_format and use_gpu.
  """
test_configs = [("NDHWC", False), ("NDHWC", True)]
if test.is_gpu_available(cuda_only=True):
    # "NCHW" format is currently supported exclusively on CUDA GPUs.
    test_configs += [("NCDHW", True)]
exit(test_configs)
