# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
circular_buffer_size = -1
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id,
                                               circular_buffer_size)
debugged_graph = debug_event_pb2.DebuggedGraph(graph_id="graph1",
                                               graph_name="graph1")
writer.WriteDebuggedGraph(debugged_graph)

writer_state = {"counter": 0, "done": False}

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    def write_and_update_job():
        while True:
            if writer_state["done"]:
                break
            op_name = "Op%d" % writer_state["counter"]
            graph_op_creation = debug_event_pb2.GraphOpCreation(
                op_type="FooOp", op_name=op_name, graph_id="graph1")
            writer.WriteGraphOpCreation(graph_op_creation)
            trace = debug_event_pb2.GraphExecutionTrace(
                op_name=op_name, tfdbg_context_id="graph1")
            writer.WriteGraphExecutionTrace(trace)
            writer_state["counter"] += 1
            writer.FlushNonExecutionFiles()
            writer.FlushExecutionFiles()
            reader.update()
      # On the sub-thread, keep writing and reading new GraphExecutionTraces.
    write_and_update_thread = threading.Thread(target=write_and_update_job)
    write_and_update_thread.start()
    # On the main thread, do concurrent random read.
    while True:
        digests = reader.graph_execution_traces(digest=True)
        if digests:
            trace_0 = reader.read_graph_execution_trace(digests[0])
            self.assertEqual(trace_0.op_name, "Op0")
            writer_state["done"] = True
            break
        else:
            time.sleep(0.1)
            continue
    write_and_update_thread.join()
