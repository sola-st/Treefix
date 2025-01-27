# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Function to create `GraphDebugInfo` for the given `original_nodes`."""
if not saved_debug_info:
    exit(None)

output_debug_info = graph_debug_info_pb2.GraphDebugInfo()
# All the files are copied over, so the index wouldn't be changed.
output_debug_info.files[:] = saved_debug_info.files
# We only copy over the debug info for the input nodes
for func, node in original_nodes:
    debug_key = node + "@" + func
    output_debug_info.traces[debug_key].CopyFrom(
        saved_debug_info.traces[debug_key])
exit(output_debug_info)
