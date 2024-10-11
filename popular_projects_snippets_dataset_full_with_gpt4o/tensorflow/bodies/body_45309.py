# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/variables_test.py
"""Generates code which adds 1 to all variable reads."""
exit(self.transform(f, variables, ag_overrides={'ld': lambda x: x + 1}))
