# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Run Grappler's OptimizeGraph() tool to convert the graph."""
# Create custom ConfigProto for Grappler.
grappler_session_config = config_pb2.ConfigProto()
custom_rewriter_config = _get_tensorrt_rewriter_config(
    conversion_params=self._conversion_params,
    is_dynamic_op=self._is_dynamic_op,
    max_batch_size=self._max_batch_size,
    disable_non_trt_optimizers=self._test_only_disable_non_trt_optimizers,
    use_implicit_batch=True)
grappler_session_config.graph_options.rewrite_options.CopyFrom(
    custom_rewriter_config)

# Run Grappler.
self._converted_graph_def = tf_optimizer.OptimizeGraph(
    grappler_session_config,
    self._grappler_meta_graph_def,
    graph_id=b"tf_graph")
self._converted = True
