# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
expected_engines = self.ExpectedEnginesToBuild(run_params)
num_engines = 0
functions = [f.signature.name for f in gdef_to_verify.library.function]
for node in gdef_to_verify.node:
    if node.op == "TRTEngineOp":
        logging.info("Found TRTEngineOp: " + node.name)
        num_engines += 1
        segment_funcdef_name = node.attr["segment_func"].func.name
        function_name = node.name + "_native_segment"
        is_dynamic_engine = not node.attr["static_engine"].b
        self.assertNotEmpty(segment_funcdef_name, node.name)
        self.assertIn(function_name, functions)
        if (not IsQuantizationWithCalibration(run_params) and
            not is_dynamic_engine):
            self.assertTrue(len(node.attr["serialized_segment"].s), node.name)
        self.assertIn(
            self._RemoveGraphSequenceNumber(node.name), expected_engines)
        if IsQuantizationWithoutCalibration(run_params):
            # TODO(bixia): Refine this check by inspecting nodes in the engine.
            if self._ToBytes("INT8") != node.attr["precision_mode"].s:
                self.assertEqual(
                    self._ToBytes("FP16"), node.attr["precision_mode"].s, node.name)
        else:
            self.assertEqual(
                self._ToBytes(run_params.precision_mode),
                node.attr["precision_mode"].s, node.name)

        self.assertEqual(run_params.dynamic_engine, is_dynamic_engine,
                         node.name)
        self.assertEqual(node.attr["use_calibration"].b,
                         run_params.use_calibration, node.name)

        has_calibration_data = len(node.attr["calibration_data"].s)
        if (IsQuantizationWithCalibration(run_params) and
            graph_state == GraphState.INFERENCE):
            self.assertTrue(has_calibration_data, node.name)
        else:
            self.assertFalse(has_calibration_data, node.name)
if graph_state == GraphState.ORIGINAL:
    self.assertEqual(0, num_engines)
else:
    self.assertEqual(num_engines, len(expected_engines))
    expected_connections = self.ExpectedConnections(run_params)
    if expected_connections:
        self._VerifyConnections(expected_engines, expected_connections,
                                original_gdef, gdef_to_verify)
    self._VerifyMaxBatchSizeAnnotations(
        expected_engines=expected_engines,
        original_gdef=original_gdef,
        converted_gdef=gdef_to_verify,
        expected_max_batch_sizes=self.ExpectedMaxBatchSizes(run_params),
        default_max_batch_size=self.GetMaxBatchSize(run_params))
