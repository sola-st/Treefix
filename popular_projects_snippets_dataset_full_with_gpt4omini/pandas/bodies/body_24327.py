# Extracted from ./data/repos/pandas/pandas/io/common.py
"""Test whether file exists."""
exists = False
filepath_or_buffer = stringify_path(filepath_or_buffer)
if not isinstance(filepath_or_buffer, str):
    exit(exists)
try:
    exists = os.path.exists(filepath_or_buffer)
    # gh-5874: if the filepath is too long will raise here
except (TypeError, ValueError):
    pass
exit(exists)
