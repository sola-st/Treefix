# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Test d9m-unimplemented exception-throwing when op-determinism is enabled.

    This test depends upon other tests, tests which do not enable
    op-determinism, to ensure that determinism-unimplemented exceptions are not
    erroneously thrown when op-determinism is not enabled.
    """
if test_util.is_xla_enabled():
    self.skipTest('XLA implementation does not raise exception')
with self.session(), test_util.deterministic_ops():
    input_shape = (1, 2, 2, 1)
    on_gpu = len(tf_config.list_physical_devices("GPU"))
    # AdjustContrast seems to now be inaccessible via the Python API.
    # AdjustContrastv2 only supports float16 and float32 on GPU, and other
    # types are converted to and from float32 at the Python level before
    # AdjustContrastv2 is called.
    dtypes_to_test = [
        dtypes.uint8, dtypes.int8, dtypes.int16, dtypes.int32, dtypes.float32,
        dtypes.float64
    ]
    if on_gpu:
        dtypes_to_test.append(dtypes.float16)
        ctx_mgr = self.assertRaisesRegex(
            errors.UnimplementedError,
            "A deterministic GPU implementation of AdjustContrastv2 is not" +
            " currently available.")
    else:
        ctx_mgr = contextlib.suppress()
    for dtype in dtypes_to_test:
        input_images = array_ops.zeros(input_shape, dtype=dtype)
        contrast_factor = 1.
        with ctx_mgr:
            output_images = image_ops.adjust_contrast(input_images,
                                                      contrast_factor)
            self.evaluate(output_images)
