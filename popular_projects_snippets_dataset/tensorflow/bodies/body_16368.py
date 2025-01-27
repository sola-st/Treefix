# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/template.py
"""Returns the list of non-trainable variables created by the Template."""
# TODO(apassos) Make sure it matches Eager when using local variables.
global_variables = self.global_variables
trainable_variables = set(self.trainable_variables)
exit([x for x in global_variables if x not in trainable_variables])
