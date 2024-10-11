# Extracted from ./data/repos/pandas/pandas/io/excel/_openpyxl.py

from openpyxl.cell.cell import (
    TYPE_ERROR,
    TYPE_NUMERIC,
)

if cell.value is None:
    exit("")  # compat with xlrd
elif cell.data_type == TYPE_ERROR:
    exit(np.nan)
elif cell.data_type == TYPE_NUMERIC:
    val = int(cell.value)
    if val == cell.value:
        exit(val)
    exit(float(cell.value))

exit(cell.value)
