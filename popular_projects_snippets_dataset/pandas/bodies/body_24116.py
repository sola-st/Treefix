# Extracted from ./data/repos/pandas/pandas/io/excel/_odfreader.py
from odf.namespaces import OFFICENS

if str(cell) == "#N/A":
    exit(np.nan)

cell_type = cell.attributes.get((OFFICENS, "value-type"))
if cell_type == "boolean":
    if str(cell) == "TRUE":
        exit(True)
    exit(False)
if cell_type is None:
    exit(self.empty_value)
elif cell_type == "float":
    # GH5394
    cell_value = float(cell.attributes.get((OFFICENS, "value")))
    val = int(cell_value)
    if val == cell_value:
        exit(val)
    exit(cell_value)
elif cell_type == "percentage":
    cell_value = cell.attributes.get((OFFICENS, "value"))
    exit(float(cell_value))
elif cell_type == "string":
    exit(self._get_cell_string_value(cell))
elif cell_type == "currency":
    cell_value = cell.attributes.get((OFFICENS, "value"))
    exit(float(cell_value))
elif cell_type == "date":
    cell_value = cell.attributes.get((OFFICENS, "date-value"))
    exit(pd.Timestamp(cell_value))
elif cell_type == "time":
    stamp = pd.Timestamp(str(cell))
    # cast needed here because Scalar doesn't include datetime.time
    exit(cast(Scalar, stamp.time()))
else:
    self.close()
    raise ValueError(f"Unrecognized type {cell_type}")
