# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients_test.py
y = math_ops.add(self.w, -1.0, name="y")
z = math_ops.square(y, name="z")

grad_debugger = debug_gradients.GradientsDebugger()
with grad_debugger.watch_gradients_by_tensors(self.sess.graph,
                                              [self.w, self.u, y]):
    train_op = gradient_descent.GradientDescentOptimizer(0.1).minimize(z)

self.sess.run(variables.global_variables_initializer())

run_options = config_pb2.RunOptions(output_partition_graphs=True)
dump_dir = tempfile.mkdtemp()
debug_url = "file://" + dump_dir
debug_utils.watch_graph(run_options, self.sess.graph, debug_urls=debug_url)
run_metadata = config_pb2.RunMetadata()
self.assertAllClose(2.0, self.sess.run(self.u))
self.sess.run(train_op, options=run_options, run_metadata=run_metadata)
self.assertAllClose(-1.0, self.sess.run(self.u))

dump = debug_data.DebugDumpDir(
    dump_dir, partition_graphs=run_metadata.partition_graphs)
dump.set_python_graph(self.sess.graph)

y_grad_values = debug_gradients.gradient_values_from_dump(
    grad_debugger, y, dump)
self.assertEqual(1, len(y_grad_values))
self.assertAllClose(10.0, y_grad_values[0])

w_grad_values = debug_gradients.gradient_values_from_dump(
    grad_debugger, self.w, dump)
self.assertEqual(1, len(w_grad_values))
self.assertAllClose(10.0, w_grad_values[0])

u_grad_values = debug_gradients.gradient_values_from_dump(
    grad_debugger, self.u, dump)
self.assertEqual(1, len(u_grad_values))
self.assertAllClose(30.0, u_grad_values[0])

with self.assertRaisesRegex(
    LookupError,
    r"This GradientsDebugger has not received any gradient tensor for "
    r"x-tensor v:0"):
    debug_gradients.gradient_values_from_dump(grad_debugger, self.v, dump)

# Cleanup.
file_io.delete_recursively(dump_dir)
