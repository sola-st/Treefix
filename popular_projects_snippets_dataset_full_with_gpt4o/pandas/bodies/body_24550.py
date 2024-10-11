# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
for row_num in range(len(self.strrows)):
    if row_num >= self._header_row_num:
        exit(self.get_strrow(row_num))
