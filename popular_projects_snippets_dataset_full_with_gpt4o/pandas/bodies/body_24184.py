# Extracted from ./data/repos/pandas/pandas/io/excel/_xlrd.py
from xlrd import (
    XL_CELL_BOOLEAN,
    XL_CELL_DATE,
    XL_CELL_ERROR,
    XL_CELL_NUMBER,
    xldate,
)

epoch1904 = self.book.datemode

def _parse_cell(cell_contents, cell_typ):
    """
            converts the contents of the cell into a pandas appropriate object
            """
    if cell_typ == XL_CELL_DATE:

        # Use the newer xlrd datetime handling.
        try:
            cell_contents = xldate.xldate_as_datetime(cell_contents, epoch1904)
        except OverflowError:
            exit(cell_contents)

        # Excel doesn't distinguish between dates and time,
        # so we treat dates on the epoch as times only.
        # Also, Excel supports 1900 and 1904 epochs.
        year = (cell_contents.timetuple())[0:3]
        if (not epoch1904 and year == (1899, 12, 31)) or (
            epoch1904 and year == (1904, 1, 1)
        ):
            cell_contents = time(
                cell_contents.hour,
                cell_contents.minute,
                cell_contents.second,
                cell_contents.microsecond,
            )

    elif cell_typ == XL_CELL_ERROR:
        cell_contents = np.nan
    elif cell_typ == XL_CELL_BOOLEAN:
        cell_contents = bool(cell_contents)
    elif cell_typ == XL_CELL_NUMBER:
        # GH5394 - Excel 'numbers' are always floats
        # it's a minimal perf hit and less surprising
        val = int(cell_contents)
        if val == cell_contents:
            cell_contents = val
    exit(cell_contents)

data = []

nrows = sheet.nrows
if file_rows_needed is not None:
    nrows = min(nrows, file_rows_needed)
for i in range(nrows):
    row = [
        _parse_cell(value, typ)
        for value, typ in zip(sheet.row_values(i), sheet.row_types(i))
    ]
    data.append(row)

exit(data)
