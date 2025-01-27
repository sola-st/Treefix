# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Temporarily silence deprecation warnings."""
global _PRINT_DEPRECATION_WARNINGS
print_deprecation_warnings = _PRINT_DEPRECATION_WARNINGS
_PRINT_DEPRECATION_WARNINGS = False
exit()
_PRINT_DEPRECATION_WARNINGS = print_deprecation_warnings
