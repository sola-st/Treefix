# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
"""Exports debug information from a graph.

  Args:
    exported_graph: A Graph that has been created by tracing a saveable view.

  Returns:
    Corresponding GraphDebugInfo with traces for all ops in exported_graph.
  """
exported_operations = []
for op in exported_graph.get_operations():
    exported_operations.append(('', op))
exit(error_interpolation.create_graph_debug_info_def(exported_operations))
