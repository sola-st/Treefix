# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper_test.py
self._tmp_dir = tempfile.mkdtemp()

self.v = variables.VariableV1(10.0, name="v")
self.w = variables.VariableV1(21.0, name="w")
self.delta = constant_op.constant(1.0, name="delta")
self.inc_v = state_ops.assign_add(self.v, self.delta, name="inc_v")

self.w_int = control_flow_ops.with_dependencies(
    [self.inc_v],
    math_ops.cast(self.w, dtypes.int32, name="w_int_inner"),
    name="w_int_outer")

self.ph = array_ops.placeholder(dtypes.float32, name="ph")
self.xph = array_ops.transpose(self.ph, name="xph")
self.m = constant_op.constant(
    [[0.0, 1.0, 2.0], [-4.0, -1.0, 0.0]], dtype=dtypes.float32, name="m")
self.y = math_ops.matmul(self.m, self.xph, name="y")

self.sparse_ph = array_ops.sparse_placeholder(
    dtypes.float32, shape=([5, 5]), name="sparse_placeholder")
self.sparse_add = sparse_ops.sparse_add(self.sparse_ph, self.sparse_ph)

rewriter_config = rewriter_config_pb2.RewriterConfig(
    disable_model_pruning=True,
    arithmetic_optimization=rewriter_config_pb2.RewriterConfig.OFF,
    dependency_optimization=rewriter_config_pb2.RewriterConfig.OFF)
graph_options = config_pb2.GraphOptions(rewrite_options=rewriter_config)
config_proto = config_pb2.ConfigProto(graph_options=graph_options)
self.sess = session.Session(config=config_proto)

# Initialize variable.
self.sess.run(variables.global_variables_initializer())
