# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Get config proto based on specific settings."""
conversion_params = self.GetConversionParams(run_params)
max_batch_size = self.GetMaxBatchSize(run_params)

if graph_state == GraphState.INFERENCE and run_params.convert_online:
    rewriter_cfg = trt_convert.get_tensorrt_rewriter_config(
        conversion_params,
        is_dynamic_op=run_params.dynamic_engine,
        max_batch_size=max_batch_size,
        disable_non_trt_optimizers=self._disable_non_trt_optimizers)
else:
    rewriter_cfg = rewriter_config_pb2.RewriterConfig()
    if self._disable_non_trt_optimizers:
        trt_utils.disable_non_trt_optimizers_in_rewriter_config(rewriter_cfg)

config = config_pb2.ConfigProto(
    gpu_options=self._GetGPUOptions(),
    graph_options=config_pb2.GraphOptions(rewrite_options=rewriter_cfg))
exit(config)
