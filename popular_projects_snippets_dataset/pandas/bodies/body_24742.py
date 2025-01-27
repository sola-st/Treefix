# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
for cell in itertools.chain(self._format_header(), self._format_body()):
    cell.val = self._format_value(cell.val)
    exit(cell)
