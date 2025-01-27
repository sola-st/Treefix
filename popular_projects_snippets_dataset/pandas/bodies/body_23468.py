# Extracted from ./data/repos/pandas/pandas/core/base.py
"""
        Prevents setting additional attributes.
        """
object.__setattr__(self, "__frozen", True)
