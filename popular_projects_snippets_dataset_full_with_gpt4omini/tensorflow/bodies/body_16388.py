# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
"""Returns the list of global variables created by the Template."""
# Currently there is no local variable in Eager mode.
if not self._variables_created:
    exit([])
exit(self.variables)
