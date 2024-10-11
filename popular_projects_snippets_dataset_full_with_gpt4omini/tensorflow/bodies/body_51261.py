# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Exports debug information from graph to file.

  Creates and writes GraphDebugInfo with traces for ops in all functions of the
  exported_graph.

  Args:
    exported_graph: A Graph that has been created by tracing a saveable view.
    export_dir: SavedModel directory in which to write the debug info.
  """
exported_operations = []
for fn_name in exported_graph._functions:  # pylint: disable=protected-access
    fn = exported_graph._get_function(fn_name)  # pylint: disable=protected-access
    if not isinstance(fn, defun._EagerDefinedFunction):  # pylint: disable=protected-access
        continue

    fn_graph = fn.graph
    for fn_op in fn_graph.get_operations():
        exported_operations.append((fn_name, fn_op))

graph_debug_info = error_interpolation.create_graph_debug_info_def(
    exported_operations)
file_io.atomic_write_string_to_file(
    file_io.join(
        path_helpers.get_or_create_debug_dir(export_dir),
        constants.DEBUG_INFO_FILENAME_PB),
    graph_debug_info.SerializeToString(deterministic=True))
