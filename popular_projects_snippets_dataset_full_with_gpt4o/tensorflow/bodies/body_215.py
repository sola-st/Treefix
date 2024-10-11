# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
self._api_change_spec = api_change_spec
self._log = []   # Holds 4-tuples: severity, line, col, msg.
self._stack = []  # Allow easy access to parents.
