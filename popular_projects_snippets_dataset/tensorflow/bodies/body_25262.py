# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Write the object itself to file, in a plain format.

    The font_attr_segs and annotations are ignored.

    Args:
      file_path: (str) path of the file to write to.
    """

with gfile.Open(file_path, "w") as f:
    for line in self._lines:
        f.write(line + "\n")
