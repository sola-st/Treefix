# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Memory usage in a form of human readable string."""
exit(f"{_sizeof_fmt(self.memory_usage_bytes, self.size_qualifier)}\n")
