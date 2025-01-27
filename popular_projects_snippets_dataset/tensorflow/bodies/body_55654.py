# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
graph = ops.Graph()
with graph.as_default():
    with ops.name_scope("queue1"):
        input_queue = data_flow_ops.FIFOQueue(10, dtypes.float32)
        enqueue = input_queue.enqueue((9876), name="enqueue")
        close = input_queue.close(name="close")
        qr = queue_runner_impl.QueueRunner(input_queue, [enqueue], close)
        queue_runner_impl.add_queue_runner(qr)
        input_queue.dequeue(name="dequeue")

    orig_meta_graph, _ = meta_graph.export_scoped_meta_graph(
        filename=os.path.join(test_dir, exported_filename),
        graph=ops.get_default_graph(),
        export_scope="queue1")

exit(orig_meta_graph)
