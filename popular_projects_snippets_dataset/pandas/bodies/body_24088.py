# Extracted from ./data/repos/pandas/pandas/io/excel/_openpyxl.py

if self.book.read_only:
    sheet.reset_dimensions()

data: list[list[Scalar]] = []
last_row_with_data = -1
for row_number, row in enumerate(sheet.rows):
    converted_row = [self._convert_cell(cell) for cell in row]
    while converted_row and converted_row[-1] == "":
        # trim trailing empty elements
        converted_row.pop()
    if converted_row:
        last_row_with_data = row_number
    data.append(converted_row)
    if file_rows_needed is not None and len(data) >= file_rows_needed:
        break

        # Trim trailing empty rows
data = data[: last_row_with_data + 1]

if len(data) > 0:
    # extend rows to max width
    max_width = max(len(data_row) for data_row in data)
    if min(len(data_row) for data_row in data) < max_width:
        empty_cell: list[Scalar] = [""]
        data = [
            data_row + (max_width - len(data_row)) * empty_cell
            for data_row in data
        ]

exit(data)
