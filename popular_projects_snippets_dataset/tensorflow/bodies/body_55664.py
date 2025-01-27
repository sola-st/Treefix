# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py

def _enqueue_vector(sess, queue, values, shape=None):
    if not shape:
        shape = (1, len(values))
    dtype = queue.dtypes[0]
    sess.run(
        queue.enqueue(constant_op.constant(
            values, dtype=dtype, shape=shape)))

meta_graph_filename = os.path.join(
    _TestDir("metrics_export"), "meta_graph.pb")

graph = ops.Graph()
with self.session(graph=graph) as sess:
    values_queue = data_flow_ops.FIFOQueue(
        4, dtypes.float32, shapes=(1, 2))
    _enqueue_vector(sess, values_queue, [0, 1])
    _enqueue_vector(sess, values_queue, [-4.2, 9.1])
    _enqueue_vector(sess, values_queue, [6.5, 0])
    _enqueue_vector(sess, values_queue, [-3.2, 4.0])
    values = values_queue.dequeue()

    _, update_op = metrics.mean(values)

    initializer = variables.local_variables_initializer()
    self.evaluate(initializer)
    self.evaluate(update_op)

meta_graph.export_scoped_meta_graph(
    filename=meta_graph_filename, graph=graph)

# Verifies that importing a meta_graph with LOCAL_VARIABLES collection
# works correctly.
graph = ops.Graph()
with self.session(graph=graph) as sess:
    meta_graph.import_scoped_meta_graph(meta_graph_filename)
    initializer = variables.local_variables_initializer()
    self.evaluate(initializer)

# Verifies that importing an old meta_graph where "local_variables"
# collection is of node_list type works, but cannot build initializer
# with the collection.
graph = ops.Graph()
with self.session(graph=graph) as sess:
    meta_graph.import_scoped_meta_graph(
        test.test_src_dir_path(
            "python/framework/testdata/metrics_export_meta_graph.pb"))
    self.assertEqual(len(ops.get_collection(ops.GraphKeys.LOCAL_VARIABLES)),
                     2)
    with self.assertRaisesRegex(
        AttributeError, "'Tensor' object has no attribute 'initializer'"):
        initializer = variables.local_variables_initializer()
