# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py
for cse in [False, True]:
    for inline in [False, True]:
        for cfold in [False, True]:
            cfg = config_pb2.ConfigProto(
                graph_options=config_pb2.GraphOptions(
                    optimizer_options=config_pb2.OptimizerOptions(
                        opt_level=config_pb2.OptimizerOptions.L0,
                        do_common_subexpression_elimination=cse,
                        do_function_inlining=inline,
                        do_constant_folding=cfold)))
            if cse:
                cfg.graph_options.rewrite_options.arithmetic_optimization = (
                    rewriter_config_pb2.RewriterConfig.ON)
            else:
                cfg.graph_options.rewrite_options.arithmetic_optimization = (
                    rewriter_config_pb2.RewriterConfig.OFF)
            if inline:
                cfg.graph_options.rewrite_options.function_optimization = (
                    rewriter_config_pb2.RewriterConfig.ON)
            else:
                cfg.graph_options.rewrite_options.function_optimization = (
                    rewriter_config_pb2.RewriterConfig.OFF)
            if cfold:
                cfg.graph_options.rewrite_options.constant_folding = (
                    rewriter_config_pb2.RewriterConfig.ON)
            else:
                cfg.graph_options.rewrite_options.constant_folding = (
                    rewriter_config_pb2.RewriterConfig.OFF)
            exit(cfg)
