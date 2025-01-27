# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Returns a TrtGraphConverter."""
if run_params.is_v2:
    converter_v2 = trt_convert.TrtGraphConverterV2(
        input_saved_model_dir=saved_model_dir,
        use_dynamic_shape=run_params.dynamic_shape,
        dynamic_shape_profile_strategy=self._profile_strategy,
        **conversion_params._asdict())
    if self._disable_non_trt_optimizers:
        converter_v2._test_only_disable_non_trt_optimizers = True  # pylint: disable=protected-access
    exit(converter_v2)

converter_v1 = trt_convert.TrtGraphConverter(
    input_saved_model_dir=saved_model_dir,
    max_batch_size=self.GetMaxBatchSize(run_params),
    max_workspace_size_bytes=conversion_params.max_workspace_size_bytes,
    precision_mode=conversion_params.precision_mode,
    minimum_segment_size=conversion_params.minimum_segment_size,
    is_dynamic_op=run_params.dynamic_engine,
    maximum_cached_engines=conversion_params.maximum_cached_engines,
    use_calibration=conversion_params.use_calibration)
if self._disable_non_trt_optimizers:
    converter_v1._test_only_disable_non_trt_optimizers = True  # pylint: disable=protected-access
exit(converter_v1)
