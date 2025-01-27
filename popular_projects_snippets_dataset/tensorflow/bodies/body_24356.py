# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
"""Create and run a TensorFlow Graph to generate debug dumps.

    This is intentionally done in separate method, to make it easier to test
    the stack-top mode of source annotation.
    """

self.dump_root = self.get_temp_dir()
self.curr_file_path = os.path.abspath(
    tf_inspect.getfile(tf_inspect.currentframe()))

# Run a simple TF graph to generate some debug dumps that can be used in
# source annotation.
with session.Session() as sess:
    self.u_init = constant_op.constant(
        np.array([[5.0, 3.0], [-1.0, 0.0]]), shape=[2, 2], name="u_init")
    self.u_init_line_number = line_number_above()

    self.u = variables.Variable(self.u_init, name="u")
    self.u_line_number = line_number_above()

    self.v_init = constant_op.constant(
        np.array([[2.0], [-1.0]]), shape=[2, 1], name="v_init")
    self.v_init_line_number = line_number_above()

    self.v = variables.Variable(self.v_init, name="v")
    self.v_line_number = line_number_above()

    self.w = math_ops.matmul(self.u, self.v, name="w")
    self.w_line_number = line_number_above()

    self.evaluate(self.u.initializer)
    self.evaluate(self.v.initializer)

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options, sess.graph, debug_urls=["file://%s" % self.dump_root])
    run_metadata = config_pb2.RunMetadata()
    sess.run(self.w, options=run_options, run_metadata=run_metadata)

    self.dump = debug_data.DebugDumpDir(
        self.dump_root, partition_graphs=run_metadata.partition_graphs)
    self.dump.set_python_graph(sess.graph)
