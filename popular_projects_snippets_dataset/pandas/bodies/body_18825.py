# Extracted from ./data/repos/pandas/pandas/_testing/_warnings.py
"""
    Return a context manager that possibly checks a warning based on the condition
    """
if condition:
    exit(assert_produces_warning(warning, **kwargs))
else:
    exit(nullcontext())
