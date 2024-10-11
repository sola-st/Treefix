# Extracted from ./data/repos/pandas/pandas/io/excel/_openpyxl.py
# Write the frame cells using openpyxl.
sheet_name = self._get_sheet_name(sheet_name)

_style_cache: dict[str, dict[str, Serialisable]] = {}

if sheet_name in self.sheets and self._if_sheet_exists != "new":
    if "r+" in self._mode:
        if self._if_sheet_exists == "replace":
            old_wks = self.sheets[sheet_name]
            target_index = self.book.index(old_wks)
            del self.book[sheet_name]
            wks = self.book.create_sheet(sheet_name, target_index)
        elif self._if_sheet_exists == "error":
            raise ValueError(
                f"Sheet '{sheet_name}' already exists and "
                f"if_sheet_exists is set to 'error'."
            )
        elif self._if_sheet_exists == "overlay":
            wks = self.sheets[sheet_name]
        else:
            raise ValueError(
                f"'{self._if_sheet_exists}' is not valid for if_sheet_exists. "
                "Valid options are 'error', 'new', 'replace' and 'overlay'."
            )
    else:
        wks = self.sheets[sheet_name]
else:
    wks = self.book.create_sheet()
    wks.title = sheet_name

if validate_freeze_panes(freeze_panes):
    freeze_panes = cast(Tuple[int, int], freeze_panes)
    wks.freeze_panes = wks.cell(
        row=freeze_panes[0] + 1, column=freeze_panes[1] + 1
    )

for cell in cells:
    xcell = wks.cell(
        row=startrow + cell.row + 1, column=startcol + cell.col + 1
    )
    xcell.value, fmt = self._value_with_fmt(cell.val)
    if fmt:
        xcell.number_format = fmt

    style_kwargs: dict[str, Serialisable] | None = {}
    if cell.style:
        key = str(cell.style)
        style_kwargs = _style_cache.get(key)
        if style_kwargs is None:
            style_kwargs = self._convert_to_style_kwargs(cell.style)
            _style_cache[key] = style_kwargs

    if style_kwargs:
        for k, v in style_kwargs.items():
            setattr(xcell, k, v)

    if cell.mergestart is not None and cell.mergeend is not None:

        wks.merge_cells(
            start_row=startrow + cell.row + 1,
            start_column=startcol + cell.col + 1,
            end_column=startcol + cell.mergeend + 1,
            end_row=startrow + cell.mergestart + 1,
        )

        # When cells are merged only the top-left cell is preserved
        # The behaviour of the other cells in a merged range is
        # undefined
        if style_kwargs:
            first_row = startrow + cell.row + 1
            last_row = startrow + cell.mergestart + 1
            first_col = startcol + cell.col + 1
            last_col = startcol + cell.mergeend + 1

            for row in range(first_row, last_row + 1):
                for col in range(first_col, last_col + 1):
                    if row == first_row and col == first_col:
                        # Ignore first cell. It is already handled.
                        continue
                    xcell = wks.cell(column=col, row=row)
                    for k, v in style_kwargs.items():
                        setattr(xcell, k, v)
