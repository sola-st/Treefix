# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/fake_summary_writer.py
self._logdir = logdir
self._graph = graph
self._summaries = {}
self._added_graphs = []
self._added_meta_graphs = []
self._added_session_logs = []
self._added_run_metadata = {}
