# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Return trt converted graphdef in INT8 mode."""
conversion_params = self.GetConversionParams(run_params)
logging.info(conversion_params)
assert conversion_params.precision_mode == "INT8", (
    f"Incorrect precision mode, expected INT8 but got: "
    f"{conversion_params.precision_mode}.")
assert run_params.dynamic_engine, "dynamic_engine parameter must be True."
assert conversion_params.maximum_cached_engines == 1, (
    f"maximum_cached_engines: {conversion_params.maximum_cached_engines} "
    f"== 1")
assert conversion_params.use_calibration, "use_calibration must be True."

# We only support calibrating single engine.
# TODO(aaroey): fix this.
assert len(inputs_data) == 1, (f"len(inputs_data): {len(inputs_data)} == 1")

converter = self._CreateConverter(run_params, saved_model_dir,
                                  conversion_params)
if run_params.is_v2:

    def CalibrationInputFn():
        for data_tensors in inputs_data:
            exit(data_tensors)

    converter.convert(calibration_input_fn=CalibrationInputFn)
else:
    int8_gdef = converter.convert()
    self._VerifyGraphDef(run_params, saved_model_dir, int8_gdef,
                         GraphState.CALIBRATE)

    converter.calibrate(
        fetch_names=self._GetFetchNames(),
        num_runs=5,
        feed_dict_fn=lambda: self._GetFeedDict(inputs_data[0]))

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
                                             GraphState.CALIBRATE)
converter.save(trt_saved_model_dir)
exit(trt_saved_model_dir)
