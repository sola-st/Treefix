# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
source_file = debug_event_pb2.SourceFile()
with source_file_state["lock"]:
    source_file.file_path = "/home/tf2user/file_%d.py" % source_file_state[
        "counter"]
    source_file_state["counter"] += 1
writer.WriteSourceFile(source_file)
# More-frequent-than-necessary concurrent flushing is not recommended,
# but tolerated.
writer.FlushNonExecutionFiles()
