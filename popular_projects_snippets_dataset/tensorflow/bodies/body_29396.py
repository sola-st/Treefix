# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/spacetodepth_op_test.py
# NCHW is implemented for only GPU.
if data_format == "NCHW" and not test.is_gpu_available():
    exit()

assert 4 == x.ndim

def func(x):
    exit(array_ops.space_to_depth(x, block_size, data_format=data_format))

with test_util.use_gpu():
    with self.cached_session():
        theoretical, numerical = gradient_checker_v2.compute_gradient(
            func, [ops.convert_to_tensor(x)])
        self.assertAllClose(theoretical, numerical, rtol=1e-2, atol=1e-2)
