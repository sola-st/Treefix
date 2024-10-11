# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote.py
"""Send the tracebacks of a TensorFlow execution call.

  To gRPC debug server(s). This applies to graph execution (`tf.Session.run()`)
  calls and eager execution calls.

  If `send_source`, also sends the underlying source files outside the
  TensorFlow library.

  Args:
    destinations: gRPC destination addresses, a `str` or a `list` of `str`s,
      e.g., "localhost:4242". If a `list`, gRPC requests containing the same
      `CallTraceback` proto payload will be sent to all the destinations.
    origin_stack: The traceback stack for the origin of the execution call. For
      graph execution, this is the traceback of the `tf.Session.run()`
      invocation. For eager execution, this is the traceback of the Python
      line that executes the eager operation.
    is_eager_execution: (`bool`) whether an eager execution call (i.e., not a
      `tf.Session.run` or derived methods) is being sent.
    call_key: The key of the execution call, as a string. For graph execution,
      this is a string describing the feeds, fetches (and targets) names of the
      `tf.Session.run` call. For eager execution, this is ignored.
    graph: A Python `tf.Graph` object (i.e., *not* a `tf.compat.v1.GraphDef`),
      which contains op tracebacks, if applicable.
    send_source: Whether the source files involved in the op tracebacks but
      outside the TensorFlow library are to be sent.
  """
if not isinstance(destinations, list):
    destinations = [destinations]
# Strip grpc:// prefix, if any is present.
destinations = [
    dest[len(common.GRPC_URL_PREFIX):]
    if dest.startswith(common.GRPC_URL_PREFIX) else dest
    for dest in destinations]

call_type = (debug_service_pb2.CallTraceback.EAGER_EXECUTION
             if is_eager_execution
             else debug_service_pb2.CallTraceback.GRAPH_EXECUTION)
graph_traceback = tfprof_logger.merge_default_with_oplog(
    graph, add_trainable_var=False) if graph else None
call_traceback = debug_service_pb2.CallTraceback(
    call_type=call_type, call_key=call_key, graph_traceback=graph_traceback,
    graph_version=graph.version if graph else None)

_format_origin_stack(origin_stack, call_traceback)

if send_source:
    source_file_paths = set()
    source_file_paths.update(_source_file_paths_outside_tensorflow_py_library(
        (log_entry.code_def for log_entry
         in call_traceback.graph_traceback.log_entries),
        call_traceback.graph_traceback.id_to_string))
    source_file_paths.update(_source_file_paths_outside_tensorflow_py_library(
        [call_traceback.origin_stack], call_traceback.origin_id_to_string))

    debugged_source_files = []
    for file_path in source_file_paths:
        source_files = debug_pb2.DebuggedSourceFiles()
        _load_debugged_source_file(
            file_path, source_files.source_files.add())
        debugged_source_files.append(source_files)

for destination in destinations:
    no_max_message_sizes = [("grpc.max_receive_message_length", -1),
                            ("grpc.max_send_message_length", -1)]
    channel = grpc.insecure_channel(destination, options=no_max_message_sizes)
    stub = debug_service_pb2_grpc.EventListenerStub(channel)
    stub.SendTracebacks(call_traceback)
    if send_source:
        for source_files in debugged_source_files:
            stub.SendSourceFiles(source_files)
