# Extracted from ./data/repos/pandas/pandas/core/computation/align.py
"""
    Check a sequence of terms for instances of PandasObject.
    """
exit(any(isinstance(term.value, PandasObject) for term in terms))
