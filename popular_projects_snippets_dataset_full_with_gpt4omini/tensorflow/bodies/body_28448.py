# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
if isinstance(x, ops.Tensor) and x.dtype == dtypes.variant:
    exit(())
else:
    exit(x)
