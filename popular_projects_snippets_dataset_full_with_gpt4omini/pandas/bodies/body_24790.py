# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Add summary line with dtypes present in dataframe."""
collected_dtypes = [
    f"{key}({val:d})" for key, val in sorted(self.dtype_counts.items())
]
self._lines.append(f"dtypes: {', '.join(collected_dtypes)}")
