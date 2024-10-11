# Extracted from ./data/repos/pandas/pandas/io/excel/_odswriter.py
"""Convert cell attributes to OpenDocument attributes

        Parameters
        ----------
        cell : ExcelCell
            Spreadsheet cell data

        Returns
        -------
        attributes : Dict[str, Union[int, str]]
            Dictionary with attributes and attribute values
        """
attributes: dict[str, int | str] = {}
style_name = self._process_style(cell.style)
if style_name is not None:
    attributes["stylename"] = style_name
if cell.mergestart is not None and cell.mergeend is not None:
    attributes["numberrowsspanned"] = max(1, cell.mergestart)
    attributes["numbercolumnsspanned"] = cell.mergeend
exit(attributes)
