# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py

with disable_tensorfloat32():
    with trace.Trace(run_params.test_name):
        should_run, reason_for_skipping = self.ShouldRunTest(run_params)
        if not should_run:
            exit(self.skipTest(reason_for_skipping))

        saved_model_dir = self._MakeSavedModel(run_params)

        np.random.seed(12345)  # Fix the seed so the test is deterministic.
        inputs_data = []
        input_specs = self._GetParamsCached().input_specs
        for dim_list in self._GetParamsCached().input_dims:
            assert len(input_specs) == len(dim_list), (
                f"Inconsistent input_specs and dim_list: len({input_specs}) != "
                f"len({dim_list}).")
            current_input_data = []
            for spec, np_shape in zip(input_specs, dim_list):
                np_dtype = spec.dtype.as_numpy_dtype()
                if not np.issubdtype(np_dtype, np.bool_):
                    # Multiply the input by some constant to avoid all zeros input for
                    # integer types.
                    scale = 10.0 if np.issubdtype(np_dtype, np.integer) else 1.0
                    data = (scale *
                            np.random.random_sample(np_shape)).astype(np_dtype)
                else:
                    data = np.random.choice(a=[False, True], size=np_shape)

                if run_params.is_v2:
                    with ops.device("/GPU:0"):
                        data = ops.convert_to_tensor(data)
                current_input_data.append(data)
            inputs_data.append(current_input_data)

        # Verify the original graph.
        self._VerifyGraphDef(run_params, saved_model_dir, saved_model_dir,
                             GraphState.ORIGINAL)

        # Run the original graph without TensorRT to get the reference result.
        logging.info("Running original graph w/o TensorRT\n")
        ref_result = self._RunGraph(
            run_params,
            saved_model_dir,
            inputs_data,
            GraphState.ORIGINAL,
            num_runs=1)

        # Run calibration if necessary.
        if IsQuantizationWithCalibration(run_params):
            infer_saved_model_dir = self._GetCalibratedInferGraph(
                run_params, saved_model_dir, inputs_data)
            self._VerifyGraphDef(run_params, saved_model_dir,
                                 infer_saved_model_dir, GraphState.INFERENCE)
        elif not run_params.convert_online:
            infer_saved_model_dir = self._GetInferGraph(run_params,
                                                        saved_model_dir)
            self._VerifyGraphDef(run_params, saved_model_dir,
                                 infer_saved_model_dir, GraphState.INFERENCE)
        else:
            infer_saved_model_dir = saved_model_dir

        # Run the inference graph, either using the converted graph or the
        # original graph with convert_online == True.
        logging.info("Running final inference graph\n")
        result = self._RunGraph(run_params, infer_saved_model_dir, inputs_data,
                                GraphState.INFERENCE)
        self.assertAllClose(
            ref_result,
            result,
            atol=self.ExpectedAbsoluteTolerance(run_params),
            rtol=self.ExpectedRelativeTolerance(run_params))
