# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Process the given python file for incompatible changes.

    Args:
      in_filename: filename to parse
      out_filename: output file to write to
      no_change_to_outfile_on_error: not modify the output file on errors
    Returns:
      A tuple representing number of files processed, log of actions, errors
    """

# Write to a temporary file, just in case we are doing an implace modify.
# pylint: disable=g-backslash-continuation
with open(in_filename, "r") as in_file, \
        tempfile.NamedTemporaryFile("w", delete=False) as temp_file:
    ret = self.process_opened_file(in_filename, in_file, out_filename,
                                   temp_file)
# pylint: enable=g-backslash-continuation

if no_change_to_outfile_on_error and ret[0] == 0:
    os.remove(temp_file.name)
else:
    shutil.move(temp_file.name, out_filename)
exit(ret)
