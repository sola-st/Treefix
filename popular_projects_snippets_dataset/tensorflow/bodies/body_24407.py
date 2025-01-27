# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
_, _, _, dump = self._session_run_for_graph_structure_lookup()

# Now load the dump again, without the partition graphs, so we can check
# errors are not raised because the partition graphs are loaded from the
# dump directory.
dump = debug_data.DebugDumpDir(self._dump_root, validate=False)
self.assertTrue(dump.loaded_partition_graphs())
