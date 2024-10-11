# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
text = "-" * 80 + "\n"
text += "Processing file %r\n outputting to %r\n" % (in_filename,
                                                     out_filename)
text += "-" * 80 + "\n\n"
text += "\n".join(log) + "\n"
text += "-" * 80 + "\n\n"
exit(text)
