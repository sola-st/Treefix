# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
"""Gets the mnist function.

    Args:
      use_trt: whether use TF-TRT to convert the graph.
      model_dir: the model directory to load the checkpoints.
      use_dynamic_shape: whether to run the TF-TRT conversion in dynamic shape
        mode.

    Returns:
      The mnist model function.
    """
with tempfile.TemporaryDirectory() as tmpdir:
    saved_model_dir = os.path.join(tmpdir, 'mnist')
    self._SaveModel(model_dir, saved_model_dir)

    if use_trt:
        conv_params = trt_convert.TrtConversionParams(
            precision_mode='FP16',
            minimum_segment_size=2,
            max_workspace_size_bytes=(
                trt_convert.DEFAULT_TRT_MAX_WORKSPACE_SIZE_BYTES),
            maximum_cached_engines=1)
        converter = trt_convert.TrtGraphConverterV2(
            input_saved_model_dir=saved_model_dir,
            use_dynamic_shape=use_dynamic_shape,
            dynamic_shape_profile_strategy='ImplicitBatchModeCompatible',
            **conv_params._asdict())
        converter.convert()
        try:
            line_length = max(160, os.get_terminal_size().columns)
        except OSError:
            line_length = 160
        converter.summary(line_length=line_length, detailed=True)
        func = converter._converted_func
    else:
        saved_model_loaded = saved_model_load(
            saved_model_dir, tags=[tag_constants.SERVING])
        func = saved_model_loaded.signatures[
            signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
exit(func)
