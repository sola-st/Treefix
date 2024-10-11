# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
circular_buffer_size = -1
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id,
                                               circular_buffer_size)

writer_state = {"counter": 0, "done": False}

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    def write_and_update_job():
        while True:
            if writer_state["done"]:
                break
            execution = debug_event_pb2.Execution()
            execution.op_type = "OpType%d" % writer_state["counter"]
            writer_state["counter"] += 1
            writer.WriteExecution(execution)
            writer.FlushExecutionFiles()
            reader.update()
      # On the sub-thread, keep writing and reading new Execution protos.
    write_and_update_thread = threading.Thread(target=write_and_update_job)
    write_and_update_thread.start()
    # On the main thread, do concurrent random read.
    while True:
        exec_digests = reader.executions(digest=True)
        if exec_digests:
            exec_0 = reader.read_execution(exec_digests[0])
            self.assertEqual(exec_0.op_type, "OpType0")
            writer_state["done"] = True
            break
        else:
            time.sleep(0.1)
            continue
    write_and_update_thread.join()
