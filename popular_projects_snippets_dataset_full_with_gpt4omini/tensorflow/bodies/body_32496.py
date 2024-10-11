# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
config = config_pb2.ConfigProto()
off = rewriter_config_pb2.RewriterConfig.OFF
config.graph_options.optimizer_options.opt_level = -1
config.graph_options.rewrite_options.disable_model_pruning = 1
config.graph_options.rewrite_options.constant_folding = off
config.graph_options.rewrite_options.layout_optimizer = off
config.graph_options.rewrite_options.arithmetic_optimization = off
config.graph_options.rewrite_options.dependency_optimization = off
exit(config)
