# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
"""
        search order for local (i.e., @variable) variables:

        scope, key_variable
        [('locals', 'local_name'),
         ('globals', 'local_name'),
         ('locals', 'key'),
         ('globals', 'key')]
        """
key = self.name

# if it's a variable name (otherwise a constant)
if isinstance(key, str):
    self.env.swapkey(self.local_name, key, new_value=value)

self.value = value
