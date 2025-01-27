# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
device_type = get_device().device_type
# Some dtypes are not supported on some devices
if (dtype == dtypes.bfloat16 and device_type == 'GPU' and
    not test_util.is_gpu_available(
        cuda_only=True, min_cuda_compute_capability=(8, 0))):
    dtype = dtypes.float32
shape_ = (constant_op.constant(shape, dtype=shape_dtype)
          if shape_dtype is not None else shape)
exit(op(seed=seed, shape=shape_, dtype=dtype, **kwargs))
