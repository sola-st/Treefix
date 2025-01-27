# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
log_string = "%d:%d: %s: %s" % (log[1], log[2], log[0], log[3])
if in_filename:
    exit(in_filename + ":" + log_string)
else:
    exit(log_string)
