# Extracted from ./data/repos/pandas/pandas/io/excel/_odswriter.py
"""
        Write the frame cells using odf
        """
from odf.table import (
    Table,
    TableCell,
    TableRow,
)
from odf.text import P

sheet_name = self._get_sheet_name(sheet_name)
assert sheet_name is not None

if sheet_name in self.sheets:
    wks = self.sheets[sheet_name]
else:
    wks = Table(name=sheet_name)
    self.book.spreadsheet.addElement(wks)

if validate_freeze_panes(freeze_panes):
    freeze_panes = cast(Tuple[int, int], freeze_panes)
    self._create_freeze_panes(sheet_name, freeze_panes)

for _ in range(startrow):
    wks.addElement(TableRow())

rows: DefaultDict = defaultdict(TableRow)
col_count: DefaultDict = defaultdict(int)

for cell in sorted(cells, key=lambda cell: (cell.row, cell.col)):
    # only add empty cells if the row is still empty
    if not col_count[cell.row]:
        for _ in range(startcol):
            rows[cell.row].addElement(TableCell())

            # fill with empty cells if needed
    for _ in range(cell.col - col_count[cell.row]):
        rows[cell.row].addElement(TableCell())
        col_count[cell.row] += 1

    pvalue, tc = self._make_table_cell(cell)
    rows[cell.row].addElement(tc)
    col_count[cell.row] += 1
    p = P(text=pvalue)
    tc.addElement(p)

# add all rows to the sheet
if len(rows) > 0:
    for row_nr in range(max(rows.keys()) + 1):
        wks.addElement(rows[row_nr])
