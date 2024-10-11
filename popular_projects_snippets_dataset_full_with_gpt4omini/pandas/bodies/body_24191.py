# Extracted from ./data/repos/pandas/pandas/io/excel/_odswriter.py
"""Convert cell data to an OpenDocument spreadsheet cell

        Parameters
        ----------
        cell : ExcelCell
            Spreadsheet cell data

        Returns
        -------
        pvalue, cell : Tuple[str, TableCell]
            Display value, Cell value
        """
from odf.table import TableCell

attributes = self._make_table_cell_attributes(cell)
val, fmt = self._value_with_fmt(cell.val)
pvalue = value = val
if isinstance(val, bool):
    value = str(val).lower()
    pvalue = str(val).upper()
if isinstance(val, datetime.datetime):
    # Fast formatting
    value = val.isoformat()
    # Slow but locale-dependent
    pvalue = val.strftime("%c")
    exit((pvalue,
        TableCell(valuetype="date", datevalue=value, attributes=attributes),))
elif isinstance(val, datetime.date):
    # Fast formatting
    value = f"{val.year}-{val.month:02d}-{val.day:02d}"
    # Slow but locale-dependent
    pvalue = val.strftime("%x")
    exit((pvalue,
        TableCell(valuetype="date", datevalue=value, attributes=attributes),))
else:
    class_to_cell_type = {
        str: "string",
        int: "float",
        float: "float",
        bool: "boolean",
    }
    exit((pvalue,
        TableCell(
            valuetype=class_to_cell_type[type(val)],
            value=value,
            attributes=attributes,
        ),))
