# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Add line containing memory usage."""
self._lines.append(f"memory usage: {self.memory_usage_string}")
