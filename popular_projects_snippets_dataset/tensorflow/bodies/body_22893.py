# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/run_models.py
"""Runs all sample models based on a key varying parameter."""
for model_config in self._configs:
    # Loads, compiles, calibrates and runs models.
    manager = self._model_handler_manager_cls(
        name=test_name,
        model_config=model_config,
        default_trt_convert_params=default_trt_converter_params,
        trt_convert_params_updater=trt_converter_params_updater)
    inputs = manager.generate_random_inputs()
    # As all the data are randomly generated, directly use inference data as
    # calibration data to produce reliable dynamic ranges.
    manager.convert(inputs)
    test_results = manager.run(inputs)

    # Analyzes the latency and numerical results.
    analysis_result_df, _, acc_hist = self._analyzer.analysis(test_results)

    # Outputs the analysis results
    model_name = os.path.split(manager.model_config.saved_model_dir)[-1]
    model_dir = os.path.join(self._output_dir, model_name)
    gfile.MkDir(model_dir)
    test_dir = os.path.join(model_dir, test_name)
    gfile.MkDir(test_dir)
    with gfile.Open(
        os.path.join(test_dir, "default_tensorrt_params.txt"), "w") as f:
        f.write(repr(default_trt_converter_params))
    with gfile.Open(os.path.join(test_dir, "accuracy_histograms.txt"),
                    "w") as f:
        [f.write(h) for h in acc_hist]
    self._write_analysis_result(analysis_result_df, test_dir)
