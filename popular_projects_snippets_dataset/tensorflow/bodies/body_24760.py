# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer.py
"""Construct a DebugEventsWriter object.

    NOTE: Given the same `dump_root`, all objects from this constructor
      will point to the same underlying set of writers. In other words, they
      will write to the same set of debug events files in the `dump_root`
      folder.

    Args:
      dump_root: The root directory for dumping debug data. If `dump_root` does
        not exist as a directory, it will be created.
      tfdbg_run_id: Debugger Run ID.
      circular_buffer_size: Size of the circular buffer for each of the two
        execution-related debug events files: with the following suffixes: -
          .execution - .graph_execution_traces If <= 0, the circular-buffer
          behavior will be abolished in the constructed object.
    """
if not dump_root:
    raise ValueError("Empty or None dump root")
self._dump_root = dump_root
self._tfdbg_run_id = tfdbg_run_id
_pywrap_debug_events_writer.Init(self._dump_root, self._tfdbg_run_id,
                                 circular_buffer_size)
