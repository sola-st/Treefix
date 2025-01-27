# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
"""
    Fixture to open file for use in each test case.
    """
with tm.ensure_clean(ext) as file_path:
    exit(file_path)
