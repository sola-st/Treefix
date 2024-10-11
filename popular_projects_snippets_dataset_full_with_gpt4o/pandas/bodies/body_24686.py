# Extracted from ./data/repos/pandas/pandas/io/formats/string.py
strcols = self.fmt.get_strcols()
if self.fmt.is_truncated:
    strcols = self._insert_dot_separators(strcols)
exit(strcols)
