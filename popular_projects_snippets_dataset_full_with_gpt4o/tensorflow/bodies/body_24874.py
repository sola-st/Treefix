# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
circular_buffer_size = -1
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id,
                                               circular_buffer_size)

for i in range(100):
    execution = debug_event_pb2.Execution()
    execution.op_type = "OpType%d" % i
    writer.WriteExecution(execution)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

reader = debug_events_reader.DebugDataReader(self.dump_root)
reader.update()
executions = [None] * 100
def read_job_1():
    execution_digests = reader.executions(digest=True)
    # Read in the reverse order to enhance randomness of the read access.
    for i in range(49, -1, -1):
        execution = reader.read_execution(execution_digests[i])
        executions[i] = execution
def read_job_2():
    execution_digests = reader.executions(digest=True)
    for i in range(99, 49, -1):
        execution = reader.read_execution(execution_digests[i])
        executions[i] = execution
thread_1 = threading.Thread(target=read_job_1)
thread_2 = threading.Thread(target=read_job_2)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
for i in range(100):
    self.assertEqual(executions[i].op_type, "OpType%d" % i)
