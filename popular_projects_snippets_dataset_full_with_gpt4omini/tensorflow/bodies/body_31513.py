# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
config = config_pb2.ConfigProto()
# Prevent Grappler from optimizing away the entire graph.
config.graph_options.rewrite_options.dependency_optimization = (
    rewriter_config_pb2.RewriterConfig.OFF)
with session_lib.Session(config=config) as session:
    self.evaluate(variables.global_variables_initializer())
    self.run_op_benchmark(
        session, op, burn_iters=burn_iters, min_iters=num_iters, name=name)
