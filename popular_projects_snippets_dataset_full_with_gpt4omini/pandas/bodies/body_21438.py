# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/_arrow_utils.py
"""
    Raise a PerformanceWarning for falling back to ExtensionArray's
    non-pyarrow method
    """
msg = "Falling back on a non-pyarrow code path which may decrease performance."
if version is not None:
    msg += f" Upgrade to pyarrow >={version} to possibly suppress this warning."
warnings.warn(msg, PerformanceWarning, stacklevel=find_stack_level())
