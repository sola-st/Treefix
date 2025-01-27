# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_main.py
"""Process a file of type `.py` or `.ipynb`."""

if in_filename.endswith(".py"):
    files_processed, report_text, errors = \
      upgrader.process_file(in_filename, out_filename)
elif in_filename.endswith(".ipynb"):
    files_processed, report_text, errors = \
      ipynb.process_file(in_filename, out_filename, upgrader)
else:
    raise NotImplementedError(
        "Currently converter only supports python or ipynb")

exit((files_processed, report_text, errors))
