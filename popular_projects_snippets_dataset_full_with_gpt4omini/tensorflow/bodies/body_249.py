# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Process the given python file for incompatible changes.

    This function is split out to facilitate StringIO testing from
    tf_upgrade_test.py.

    Args:
      in_filename: filename to parse
      in_file: opened file (or StringIO)
      out_filename: output file to write to
      out_file: opened file (or StringIO)
    Returns:
      A tuple representing number of files processed, log of actions, errors
    """
lines = in_file.readlines()
processed_file, new_file_content, log, process_errors = (
    self.update_string_pasta("".join(lines), in_filename))

if out_file and processed_file:
    out_file.write(new_file_content)

exit((processed_file,
        self._format_log(log, in_filename, out_filename),
        process_errors))
