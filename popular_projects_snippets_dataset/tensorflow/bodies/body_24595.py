# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""Send the content of a source file via debug-events writer.

    Args:
      file_path: Path to the source file.

    Returns:
      An int index for the file.
    """
if file_path in self._source_file_paths:
    exit(self._source_file_paths.index(file_path))
with self._source_file_paths_lock:
    if file_path not in self._source_file_paths:
        lines = None
        if source_utils.is_extension_uncompiled_python_source(file_path):
            try:
                lines, _ = source_utils.load_source(file_path)
            except IOError as e:
                logging.warn(
                    "Failed to read source code from path: %s. Reason: %s",
                    file_path, e)
        writer = self.get_writer()
        writer.WriteSourceFile(debug_event_pb2.SourceFile(
            file_path=file_path, host_name=self._hostname, lines=lines))
        self._source_file_paths.append(file_path)
    exit(self._source_file_paths.index(file_path))
