# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Writes graph_def to `logdir` and adds it to summary if applicable."""
assert self._is_chief
if self._logdir:
    training_util.write_graph(
        self._graph.as_graph_def(add_shapes=True), self._logdir,
        "graph.pbtxt")
if self._summary_writer and not self._graph_added_to_summary:
    self._summary_writer.add_graph(self._graph)
    self._summary_writer.add_meta_graph(self._meta_graph_def)
    self._graph_added_to_summary = True
