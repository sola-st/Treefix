# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
original_gdef = self._GetGraphDef(run_params,
                                  original_gdef_or_saved_model_dir)
gdef_to_verify = self._GetGraphDef(run_params,
                                   gdef_or_saved_model_dir_to_verify)
self._WriteGraph(run_params, gdef_to_verify, graph_state)
if run_params.is_v2:
    self._VerifyGraphDefV2(run_params, original_gdef, gdef_to_verify,
                           graph_state)
else:
    self._VerifyGraphDefV1(run_params, original_gdef, gdef_to_verify,
                           graph_state)
