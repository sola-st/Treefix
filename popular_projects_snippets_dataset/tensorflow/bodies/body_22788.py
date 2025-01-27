# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Get ConfigProto for session creation."""
config = config_pb2.ConfigProto(
    gpu_options=config_pb2.GPUOptions(allow_growth=True))
if rewriter_config:
    config.graph_options.rewrite_options.CopyFrom(rewriter_config)
exit(config)
