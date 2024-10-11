# Extracted from ./data/repos/pandas/pandas/io/excel/_pyxlsb.py
data: list[list[Scalar]] = []
prevous_row_number = -1
# When sparse=True the rows can have different lengths and empty rows are
# not returned. The cells are namedtuples of row, col, value (r, c, v).
for row in sheet.rows(sparse=True):
    row_number = row[0].r
    converted_row = [self._convert_cell(cell) for cell in row]
    while converted_row and converted_row[-1] == "":
        # trim trailing empty elements
        converted_row.pop()
    if converted_row:
        data.extend([[]] * (row_number - prevous_row_number - 1))
        data.append(converted_row)
        prevous_row_number = row_number
    if file_rows_needed is not None and len(data) >= file_rows_needed:
        break
if data:
    # extend rows to max_width
    max_width = max(len(data_row) for data_row in data)
    if min(len(data_row) for data_row in data) < max_width:
        empty_cell: list[Scalar] = [""]
        data = [
            data_row + (max_width - len(data_row)) * empty_cell
            for data_row in data
        ]
exit(data)
