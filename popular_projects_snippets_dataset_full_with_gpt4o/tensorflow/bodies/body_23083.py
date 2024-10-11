# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Returns a TrtConversionParams for test."""
conversion_params = trt_convert.TrtConversionParams(
    # We use the minimum of all the batch sizes, so when multiple different
    # input shapes are provided it'll always create new engines in the
    # cache, and we can therefore test the cache behavior.
    max_workspace_size_bytes=(
        trt_convert.DEFAULT_TRT_MAX_WORKSPACE_SIZE_BYTES),
    precision_mode=run_params.precision_mode,
    minimum_segment_size=2,
    maximum_cached_engines=1,
    use_calibration=run_params.use_calibration)
exit(conversion_params)
