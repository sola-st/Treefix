# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Incrementally read the .source_files DebugEvent file."""
source_files_iter = self._reader.source_files_iterator()
for debug_event, offset in source_files_iter:
    source_file = debug_event.source_file
    self._host_name_file_path_to_offset[
        (source_file.host_name, source_file.file_path)] = offset
