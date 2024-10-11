# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
if len(x_shape) == 4:
    data_format_list = ['NHWC', 'NCHW']
else:
    data_format_list = ['NCDHW', 'NDHWC']
use_gpu_vals = [False]
if test.is_gpu_available(cuda_only=True) and not cpu_only:
    use_gpu_vals += [True]
factors = [1.0, 0.6]
for dtype in [np.float16, np.float32, dtypes.bfloat16.as_numpy_dtype]:
    for use_gpu in use_gpu_vals:
        if dtype == dtypes.bfloat16.as_numpy_dtype and not use_gpu:
            continue
        for data_format in data_format_list:
            if data_format == 'NHWC' or data_format == 'NDHWC':
                scale_shape = x_shape[-1:]
            else:
                scale_shape = x_shape[1:2]
            for exponential_avg_factor in factors:
                if gradient_test:
                    self._test_gradient(
                        x_shape,
                        dtype,
                        scale_shape,
                        np.float32,
                        use_gpu=use_gpu,
                        data_format=data_format,
                        is_training=is_training,
                        exponential_avg_factor=exponential_avg_factor)
                else:
                    if is_training:
                        self._test_training(
                            x_shape,
                            dtype,
                            scale_shape,
                            np.float32,
                            use_gpu=use_gpu,
                            data_format=data_format,
                            exponential_avg_factor=exponential_avg_factor)
                    else:
                        self._test_inference(
                            x_shape,
                            dtype,
                            scale_shape,
                            np.float32,
                            use_gpu=use_gpu,
                            data_format=data_format,
                            exponential_avg_factor=exponential_avg_factor)
