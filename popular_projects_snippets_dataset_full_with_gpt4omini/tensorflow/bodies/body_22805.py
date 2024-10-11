# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""General method to test trt_convert.TrtGraphConverter()."""
output_graph_def = self._ConvertGraphV1(
    output_saved_model_dir=output_saved_model_dir,
    need_calibration=need_calibration,
    is_dynamic_op=is_dynamic_op,
    device=device)
graph_defs_to_verify = [output_graph_def]

if output_saved_model_dir:
    saved_model_graph_def = saved_model_utils.get_meta_graph_def(
        output_saved_model_dir, tag_constants.SERVING).graph_def
    self.assertIsInstance(saved_model_graph_def, graph_pb2.GraphDef)
    graph_defs_to_verify.append(saved_model_graph_def)

for graph_def in graph_defs_to_verify:
    node_name_to_op = {
        self._MayRemoveGraphSequenceNumber(node.name): node.op
        for node in graph_def.node
    }
    if device is not None and device.startswith("/CPU:"):
        self.assertEqual(
            {
                "add": "AddV2",
                "v1": "Const",
                "add_1": "AddV2",
                "add_2": "AddV2",
                "input1": "Placeholder",
                "input2": "Placeholder",
                "mul": "Mul",
                "output": "Identity"
            }, node_name_to_op)
    else:
        self.assertEqual(
            {
                "input1": "Placeholder",
                "input2": "Placeholder",
                "TRTEngineOp_000": "TRTEngineOp",
                "output": "Identity"
            }, node_name_to_op)

    if need_calibration:
        trt_engine_nodes = [
            node for node in graph_def.node if node.op == "TRTEngineOp"
        ]
        if device is not None and device.startswith("/CPU:"):
            self.assertEmpty(trt_engine_nodes)
            exit()

        self.assertNotEmpty(trt_engine_nodes)
        for node in trt_engine_nodes:
            self.assertTrue(len(node.attr["calibration_data"].s))
        # Run the calibrated graph.
        # TODO(laigd): consider having some input where the answer is different.
        with ops.Graph().as_default():
            importer.import_graph_def(graph_def, name="")
            with self.session(config=self._GetConfigProto()) as sess:
                for test_data in range(10):
                    self.assertEqual((test_data + 1.0)**2 + test_data,
                                     sess.run(
                                         "output:0",
                                         feed_dict={
                                             "input1:0": [[[test_data]]],
                                             "input2:0": [[[test_data]]]
                                         }))
