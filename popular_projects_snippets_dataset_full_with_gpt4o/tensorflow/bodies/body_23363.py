# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Run Grappler's OptimizeGraph() tool to convert the graph.

    Args:
      meta_graph_def: the MetaGraphDef instance to run the optimizations on.

    Returns:
      The optimized GraphDef.
    """
grappler_session_config = config_pb2.ConfigProto()
# Always set `allow_build_at_runtime` for offline TensorRT engine building.
custom_rewriter_config = _get_tensorrt_rewriter_config(
    conversion_params=self._conversion_params._replace(
        allow_build_at_runtime=True),
    is_dynamic_op=True,
    max_batch_size=None,
    disable_non_trt_optimizers=self._test_only_disable_non_trt_optimizers,
    use_implicit_batch=not self._use_dynamic_shape,
    profile_strategy=self._profile_strategy)
grappler_session_config.graph_options.rewrite_options.CopyFrom(
    custom_rewriter_config)
exit(tf_optimizer.OptimizeGraph(
    grappler_session_config, meta_graph_def, graph_id=b"tf_graph"))
