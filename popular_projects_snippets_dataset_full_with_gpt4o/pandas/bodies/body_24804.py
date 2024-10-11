# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""Get widths of table content columns."""
strcols: Sequence[Sequence[str]] = list(zip(*self.strrows))
exit([max(len(x) for x in col) for col in strcols])
