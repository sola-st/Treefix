# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
self._log.append((severity, lineno, col, msg))
print("%s line %d:%d: %s" % (severity, lineno, col, msg))
