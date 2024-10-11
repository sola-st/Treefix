# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation_test.py
self.assertIn(key, graph_debug_info.traces)
stack_trace = graph_debug_info.traces[key]
found_flc = None
for flc in stack_trace.file_line_cols:
    if flc.file_index == file_index:
        found_flc = flc
        break
self.assertIsNotNone(found_flc,
                     "Could not find a stack trace entry for file")
exit(found_flc)
