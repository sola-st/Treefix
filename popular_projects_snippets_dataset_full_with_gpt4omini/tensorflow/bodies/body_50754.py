# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Rewrite func names in the debug info by using the concrete func names."""
output_debug_info = graph_debug_info_pb2.GraphDebugInfo()
output_debug_info.files[:] = debug_info.files
for key in debug_info.traces:
    node, func = key.split("@")
    new_func = ""
    if func in self._concrete_functions:
        new_func = self._concrete_functions[func].function_def.signature.name
    output_debug_info.traces[node + "@" + new_func].CopyFrom(
        debug_info.traces[key])
exit(output_debug_info)
