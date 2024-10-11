# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
if config is None:
    config = config_pb2.ConfigProto(allow_soft_placement=True)
else:
    config = copy.deepcopy(config)
# Don't perform optimizations for tests so we don't inadvertently run
# gpu ops on cpu
config.graph_options.optimizer_options.opt_level = -1
config.graph_options.rewrite_options.constant_folding = (
    rewriter_config_pb2.RewriterConfig.OFF)

exit(config)
