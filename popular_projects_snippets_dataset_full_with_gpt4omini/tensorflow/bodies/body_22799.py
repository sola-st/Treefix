# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Write the saved model as an input for testing."""
g, var, inp1, inp2, out = self._GetGraphForV1(device)
signature_def = signature_def_utils.build_signature_def(
    inputs={
        "myinput1": utils.build_tensor_info(inp1),
        "myinput2": utils.build_tensor_info(inp2)
    },
    outputs={"myoutput": utils.build_tensor_info(out)},
    method_name=signature_constants.PREDICT_METHOD_NAME)
saved_model_builder = builder.SavedModelBuilder(input_saved_model_dir)
with self.session(graph=g, config=self._GetConfigProto()) as sess:
    sess.run(var.initializer)
    saved_model_builder.add_meta_graph_and_variables(
        sess, [tag_constants.SERVING],
        signature_def_map={_SAVED_MODEL_SIGNATURE_KEY: signature_def})
saved_model_builder.save()
