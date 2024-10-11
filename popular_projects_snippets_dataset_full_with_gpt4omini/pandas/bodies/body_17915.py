# Extracted from ./data/repos/pandas/pandas/tests/util/test_safe_import.py
result = td.safe_import("pandas", min_version=min_version)
result = result if valid else not result
assert result
