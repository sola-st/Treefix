# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Write the saved model as an input for testing."""
params = self._GetParamsCached()
g = ops.Graph()
with g.as_default():
    inputs = []
    for spec in params.input_specs:
        inp = array_ops.placeholder(
            dtype=spec.dtype, shape=spec.shape, name=spec.name)
        inputs.append(inp)
    outputs = params.graph_fn(*inputs)
    if not isinstance(outputs, list) and not isinstance(outputs, tuple):
        outputs = [outputs]

signature_def = signature_def_utils.build_signature_def(
    inputs={inp.op.name: utils.build_tensor_info(inp) for inp in inputs},
    outputs={out.op.name: utils.build_tensor_info(out) for out in outputs},
    method_name=signature_constants.PREDICT_METHOD_NAME)

saved_model_dir = self._GetSavedModelDir(run_params, GraphState.ORIGINAL)
saved_model_builder = builder.SavedModelBuilder(saved_model_dir)
with self.session(
    graph=g, config=self._GetConfigProto(run_params,
                                         GraphState.ORIGINAL)) as sess:
    saved_model_builder.add_meta_graph_and_variables(
        sess, [tag_constants.SERVING],
        signature_def_map={
            signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
                signature_def
        })
saved_model_builder.save()
exit(saved_model_dir)
