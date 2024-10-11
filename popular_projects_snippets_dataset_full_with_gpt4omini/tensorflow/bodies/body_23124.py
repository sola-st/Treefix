# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
params = self._GetParamsCached()
root = autotrackable.AutoTrackable()
root.run = def_function.function(
    params.graph_fn, input_signature=params.input_specs)
saved_model_dir = self._GetSavedModelDir(run_params, GraphState.ORIGINAL)
logging.info("Saving input SavedModel to %s", saved_model_dir)
save.save(root, saved_model_dir,
          {signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: root.run})
exit(saved_model_dir)
