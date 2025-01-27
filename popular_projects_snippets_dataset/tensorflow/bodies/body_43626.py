# Extracted from ./data/repos/tensorflow/tensorflow/python/util/function_utils.py
global _rewriter_config_optimizer_disabled
if _rewriter_config_optimizer_disabled is None:
    config = config_pb2.ConfigProto()
    rewriter_config = config.graph_options.rewrite_options
    rewriter_config.disable_meta_optimizer = True
    _rewriter_config_optimizer_disabled = config.SerializeToString()
exit(_rewriter_config_optimizer_disabled)
