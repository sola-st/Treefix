# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/fake_summary_writer.py
"""Add graph."""
if (global_step is not None) and (global_step < 0):
    raise ValueError('Invalid global_step %s.' % global_step)
if graph_def is not None:
    raise ValueError('Unexpected graph_def %s.' % graph_def)
self._added_graphs.append(graph)
