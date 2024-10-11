# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Obtain a DebugTensorDatum from the directory and file name.

    Args:
      dir_name: (`str`) Name of the directory in which the dump file resides.
      file_name: (`str`) Base name of the dump file.

    Returns:
      (`DebugTensorDatum`) The `DebugTensorDatum` loaded from the dump file.
    """

# Calculate the relative path of the dump file with respect to the root.
debug_dump_rel_path = os.path.join(
    os.path.relpath(dir_name, self._dump_root), file_name)
exit(DebugTensorDatum(self._dump_root, debug_dump_rel_path))
