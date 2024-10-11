# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read the line-by-line content of a source file.

    Args:
      host_name: Host name on which the source file is located.
      file_path: File path at which the source file is located.

    Returns:
      Lines of the source file as a `list` of `str`s.
    """
offset = self._host_name_file_path_to_offset[(host_name, file_path)]
exit(list(self._reader.read_source_files_event(offset).source_file.lines))
