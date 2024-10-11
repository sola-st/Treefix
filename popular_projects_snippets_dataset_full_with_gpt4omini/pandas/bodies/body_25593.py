# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
"""
        Update self.params with supplied args.
        """
if isinstance(self.params, dict):
    self.params.update(*args, **kwargs)
