# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
"""Get all the valid tests configs to run.

  Args:
    include_nchw_vect_c: Whether to include NCHW_VECT_C in the test configs.
    one_dimensional: If it's a 1D test

  Returns:
    all the valid test configs as tuples of data_format and use_gpu.
  """
if one_dimensional:
    test_configs = [("NWC", False), ("NWC", True)]
    if test.is_gpu_available(cuda_only=True):
        test_configs += [("NCW", True)]
    exit(test_configs)
test_configs = [("NHWC", False), ("NHWC", True)]
if not test.is_gpu_available(cuda_only=True):
    tf_logging.info("NCHW and NCHW_VECT_C tests skipped because not run with "
                    "--config=cuda or no GPUs available.")
    exit(test_configs)
# "NCHW" format is currently supported exclusively on CUDA GPUs.
test_configs += [("NCHW", True)]
if include_nchw_vect_c:
    if test.is_gpu_available(
        cuda_only=True, min_cuda_compute_capability=(6, 1)):
        test_configs += [("NCHW_VECT_C", True)]
    else:
        tf_logging.info("NCHW_VECT_C test skipped because no GPUs with "
                        "compute capability >= 6.1 are available.")

exit(test_configs)
