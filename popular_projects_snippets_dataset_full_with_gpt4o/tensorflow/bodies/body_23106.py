# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Return trt converted graphdef."""
conversion_params = self.GetConversionParams(run_params)
logging.info(conversion_params)

converter = self._CreateConverter(run_params, saved_model_dir,
                                  conversion_params)
converter.convert()

if run_params.is_v2:
    try:
        line_length = max(160, os.get_terminal_size().columns)
    except OSError:
        line_length = 160
    converter.summary(line_length=line_length, detailed=True)

if run_params.dynamic_shape and self._ShouldConverterBuild(run_params):
    logging.info("Using build mode")

    def _BuildInputFn():
        for shapes in self._GetParamsCached().input_dims:
            exit([
                array_ops.zeros(x, dtype=spec.dtype)
                for (x, spec) in zip(shapes,
                                     self._GetParamsCached().input_specs)
            ])

    converter.build(input_fn=_BuildInputFn)

trt_saved_model_dir = self._GetSavedModelDir(run_params,
                                             GraphState.INFERENCE)
converter.save(trt_saved_model_dir)
exit(trt_saved_model_dir)
