# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
writer = debug_events_writer.DebugEventsWriter(self.dump_root,
                                               self.tfdbg_run_id)

source_file_state = {"counter": 0, "lock": threading.Lock()}

def writer_source_file():
    source_file = debug_event_pb2.SourceFile()
    with source_file_state["lock"]:
        source_file.file_path = "/home/tf2user/file_%d.py" % source_file_state[
            "counter"]
        source_file_state["counter"] += 1
    writer.WriteSourceFile(source_file)
    # More-frequent-than-necessary concurrent flushing is not recommended,
    # but tolerated.
    writer.FlushNonExecutionFiles()

stack_frame_state = {"counter": 0, "lock": threading.Lock()}

def write_stack_frame():
    stack_frame = debug_event_pb2.StackFrameWithId()
    with stack_frame_state["lock"]:
        stack_frame.id = "stack_frame_%d" % stack_frame_state["counter"]
        stack_frame_state["counter"] += 1
    writer.WriteStackFrameWithId(stack_frame)
    # More-frequent-than-necessary concurrent flushing is not recommended,
    # but tolerated.
    writer.FlushNonExecutionFiles()

graph_op_state = {"counter": 0, "lock": threading.Lock()}

def write_graph_op_creation():
    graph_op_creation = debug_event_pb2.GraphOpCreation()
    with graph_op_state["lock"]:
        graph_op_creation.op_name = "Op%d" % graph_op_state["counter"]
        graph_op_state["counter"] += 1
    writer.WriteGraphOpCreation(graph_op_creation)
    # More-frequent-than-necessary concurrent flushing is not recommended,
    # but tolerated.
    writer.FlushNonExecutionFiles()

num_threads = 9
threads = []
for i in range(num_threads):
    if i % 3 == 0:
        target = writer_source_file
    elif i % 3 == 1:
        target = write_stack_frame
    else:
        target = write_graph_op_creation
    thread = threading.Thread(target=target)
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()

# Verify the content of the .source_files file.
with debug_events_reader.DebugEventsReader(self.dump_root) as reader:
    source_files_iter = reader.source_files_iterator()
    actuals = list(item.debug_event.source_file for item in source_files_iter)
    file_paths = sorted([actual.file_path for actual in actuals])
    self.assertEqual(file_paths, [
        "/home/tf2user/file_0.py", "/home/tf2user/file_1.py",
        "/home/tf2user/file_2.py"
    ])

# Verify the content of the .stack_frames file.
actuals = list(item.debug_event.stack_frame_with_id
               for item in reader.stack_frames_iterator())
stack_frame_ids = sorted([actual.id for actual in actuals])
self.assertEqual(stack_frame_ids,
                 ["stack_frame_0", "stack_frame_1", "stack_frame_2"])

# Verify the content of the .graphs file.
actuals = list(item.debug_event.graph_op_creation
               for item in reader.graphs_iterator())
graph_op_names = sorted([actual.op_name for actual in actuals])
self.assertEqual(graph_op_names, ["Op0", "Op1", "Op2"])
