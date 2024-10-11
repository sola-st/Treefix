# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation.py
"""Construct and returns a `GraphDebugInfo` protocol buffer.

  Args:
    func_named_operations: An iterable of (func_name, op.Operation) tuples
      where the Operation instances have a _traceback members. The func_name
      should be the empty string for operations in the top-level Graph.

  Returns:
    GraphDebugInfo protocol buffer.

  Raises:
    TypeError: If the arguments are not of the correct proto buffer type.
  """
# Creates an empty GraphDebugInfoDef proto.
graph_debug_info_def = graph_debug_info_pb2.GraphDebugInfo()

# Gets the file names and line numbers for the exported node names. Also
# collects the unique file names.
all_file_names = set()
node_to_trace = {}
for func_name, op in func_named_operations:
    if op.traceback is None:
        continue
    # Gets the stack trace of the operation and then the file location.
    node_name = op.name + "@" + func_name
    node_to_trace[node_name] = _compute_useful_frames(op.traceback, 10)
    for frame in node_to_trace[node_name]:
        all_file_names.add(frame.filename)

  # Sets the `files` field in the GraphDebugInfo proto
graph_debug_info_def.files.extend(all_file_names)

# Builds a mapping between file names and index of the `files` field, so we
# only store the indexes for the nodes in the GraphDebugInfo.
file_to_index = dict(
    [(y, x) for x, y in enumerate(graph_debug_info_def.files)])

# Creates the FileLineCol proto for each node and sets the value in the
# GraphDebugInfo proto. We only store the file name index for each node to
# save the storage space.
for node_name, frames in node_to_trace.items():
    trace_def = graph_debug_info_def.traces[node_name]
    for frame in reversed(frames):
        trace_def.file_line_cols.add(
            file_index=file_to_index[frame.filename],
            line=frame.lineno)

exit(graph_debug_info_def)
