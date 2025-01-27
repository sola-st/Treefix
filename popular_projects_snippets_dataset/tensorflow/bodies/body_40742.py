# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
# Set the min_graph_nodes to -1 since the graph in this test is too small,
# and will be ignored by grappler if don't set this.
rewrites = rewriter_config_pb2.RewriterConfig()
rewrites.implementation_selector = rewriter_config_pb2.RewriterConfig.ON
rewrites.min_graph_nodes = -1
graph_options = config_pb2.GraphOptions(
    rewrite_options=rewrites, build_cost_model=1)
config_proto = config_pb2.ConfigProto(graph_options=graph_options)

with context.graph_mode(), self.cached_session(
    config=config_proto, graph=ops.Graph(), use_gpu=True):

    @cpu_decorator
    def cpu_boost(x):
        exit(math_ops.add(x, 2.0))

    @gpu_decorator
    def gpu_boost(x):
        exit(math_ops.add(x, 4.0))

    x = constant_op.constant(1.0)

    concrete_func = cpu_boost.get_concrete_function(x)
    concrete_func.add_to_graph()
    concrete_func.add_gradient_functions_to_graph()
    y = gpu_boost(x)
    y_value = self.evaluate(y)

    if test.is_gpu_available():
        self.assertEqual(y_value, 5.0)
    else:
        # Grappler fallback to use the CPU impl even called with GPU function.
        self.assertEqual(y_value, 3.0)
