# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_utils_test.py
"""Create and run a TensorFlow Graph with a while loop to generate dumps."""

self.dump_root = self.get_temp_dir()
self.curr_file_path = os.path.abspath(
    tf_inspect.getfile(tf_inspect.currentframe()))

# Run a simple TF graph to generate some debug dumps that can be used in
# source annotation.
with session.Session() as sess:
    loop_body = lambda i: math_ops.add(i, 2)
    self.traceback_first_line = line_number_above()

    loop_cond = lambda i: math_ops.less(i, 16)

    i = constant_op.constant(10, name="i")
    loop = control_flow_ops.while_loop(loop_cond, loop_body, [i])

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options, sess.graph, debug_urls=["file://%s" % self.dump_root])
    run_metadata = config_pb2.RunMetadata()
    sess.run(loop, options=run_options, run_metadata=run_metadata)

    self.dump = debug_data.DebugDumpDir(
        self.dump_root, partition_graphs=run_metadata.partition_graphs)
    self.dump.set_python_graph(sess.graph)
