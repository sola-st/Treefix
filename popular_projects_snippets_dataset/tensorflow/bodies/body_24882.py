# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
# To simulate a multi-host data dump, we first generate file sets in two
# different directories, with the same tfdbg_run_id, and then combine them.
tfdbg_run_id = "foo"
for i in range(2):
    writer = debug_events_writer.DebugEventsWriter(
        os.path.join(self.dump_root, str(i)),
        tfdbg_run_id,
        circular_buffer_size=-1)
    if i == 0:
        debugged_graph = debug_event_pb2.DebuggedGraph(
            graph_id="graph1", graph_name="graph1")
        writer.WriteDebuggedGraph(debugged_graph)
        op_name = "Op_0"
        graph_op_creation = debug_event_pb2.GraphOpCreation(
            op_type="FooOp", op_name=op_name, graph_id="graph1")
        writer.WriteGraphOpCreation(graph_op_creation)
        op_name = "Op_1"
        graph_op_creation = debug_event_pb2.GraphOpCreation(
            op_type="FooOp", op_name=op_name, graph_id="graph1")
        writer.WriteGraphOpCreation(graph_op_creation)
    for _ in range(10):
        trace = debug_event_pb2.GraphExecutionTrace(
            op_name="Op_%d" % i, tfdbg_context_id="graph1")
        writer.WriteGraphExecutionTrace(trace)
        writer.FlushNonExecutionFiles()
        writer.FlushExecutionFiles()

    # Move all files from the subdirectory /1 to subdirectory /0.
dump_root_0 = os.path.join(self.dump_root, "0")
src_paths = glob.glob(os.path.join(self.dump_root, "1", "*"))
for src_path in src_paths:
    dst_path = os.path.join(
        dump_root_0,
        # Rename the file set to avoid file name collision.
        re.sub(r"(tfdbg_events\.\d+)", r"\g<1>1", os.path.basename(src_path)))
    os.rename(src_path, dst_path)

with debug_events_reader.DebugDataReader(dump_root_0) as reader:
    reader.update()
    # Verify the content of the .graph_execution_traces file.
    trace_digests = reader.graph_execution_traces(digest=True)
    self.assertLen(trace_digests, 20)
    for _ in range(10):
        trace = reader.read_graph_execution_trace(trace_digests[i])
        self.assertEqual(trace.op_name, "Op_0")
    for _ in range(10):
        trace = reader.read_graph_execution_trace(trace_digests[i + 10])
        self.assertEqual(trace.op_name, "Op_1")
