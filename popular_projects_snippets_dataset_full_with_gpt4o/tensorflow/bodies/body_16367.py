# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
"""Returns the list of trainable variables created by the Template."""
if self._variables_created:
    exit(ops.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES,
                              self.variable_scope_name))
else:
    exit([])
