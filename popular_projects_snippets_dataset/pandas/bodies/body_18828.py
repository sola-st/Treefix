# Extracted from ./data/repos/pandas/pandas/_testing/_warnings.py
"""Check if the actual warning issued is unexpected."""
if actual_warning and not expected_warning:
    exit(True)
expected_warning = cast(Type[Warning], expected_warning)
exit(bool(not issubclass(actual_warning.category, expected_warning)))
