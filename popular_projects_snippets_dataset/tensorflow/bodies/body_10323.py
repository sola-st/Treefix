# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
shape = config['shape']
err_tolerance = config['err_tolerance']
dtype = config['dtype']
rank = len(shape)
if rank == 4:
    data_format_nhwc, features_nhwc = 'NHWC', shape[3]
    data_format_nchw, features_nchw = 'NCHW', shape[1]
else:
    data_format_nhwc, features_nhwc = 'NDHWC', shape[4]
    data_format_nchw, features_nchw = 'NCDHW', shape[1]
for is_training in [True, False]:
    if test.is_gpu_available(cuda_only=True):
        self._test_grad_grad(
            shape,
            dtype, [features_nhwc],
            np.float32,
            use_gpu=True,
            data_format=data_format_nhwc,
            is_training=is_training,
            err_tolerance=err_tolerance)
        self._test_grad_grad(
            shape,
            dtype, [features_nchw],
            np.float32,
            use_gpu=True,
            data_format=data_format_nchw,
            is_training=is_training,
            err_tolerance=err_tolerance)
    self._test_grad_grad(
        shape,
        dtype, [features_nhwc],
        np.float32,
        use_gpu=False,
        data_format=data_format_nhwc,
        is_training=is_training,
        err_tolerance=err_tolerance)
    self._test_grad_grad(
        shape,
        dtype, [features_nchw],
        np.float32,
        use_gpu=False,
        data_format=data_format_nchw,
        is_training=is_training,
        err_tolerance=err_tolerance)
