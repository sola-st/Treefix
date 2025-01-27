# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
params = self._GetParamsCached()
for data in inputs_data:
    assert len(params.input_specs) == len(data), (
        f"Inconsistent params.input_specs and data: "
        f"len({params.input_specs}) != len({data}).")

if run_params.is_v2:
    results = self._RunGraphV2(saved_model_dir, inputs_data, graph_state,
                               num_runs)
    gc.collect()  # Force GC to destroy the TRT engine cache.
    exit(results)

# The default config for tf.session is None. Create a config with
# TensorRTOptimizer enabled to support convert_online for inference.
config = None
# TODO(b/170220818): use the default session config to run inferenence
#   graphs for the offline conversion case after fixing the bug.
if graph_state == GraphState.INFERENCE:
    config = self._GetConfigProto(run_params, GraphState.INFERENCE)
exit(self._RunGraphV1(saved_model_dir, inputs_data, config, num_runs))
