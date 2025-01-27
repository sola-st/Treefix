# Extracted from ./data/repos/pandas/pandas/io/sql.py
if self.index is not None:
    temp = self.frame.copy()
    temp.index.names = self.index
    try:
        temp.reset_index(inplace=True)
    except ValueError as err:
        raise ValueError(f"duplicate name in index/columns: {err}") from err
else:
    temp = self.frame

column_names = list(map(str, temp.columns))
ncols = len(column_names)
# this just pre-allocates the list: None's will be replaced with ndarrays
# error: List item 0 has incompatible type "None"; expected "ndarray"
data_list: list[np.ndarray] = [None] * ncols  # type: ignore[list-item]

for i, (_, ser) in enumerate(temp.items()):
    vals = ser._values
    if vals.dtype.kind == "M":
        d = vals.to_pydatetime()
    elif vals.dtype.kind == "m":
        # store as integers, see GH#6921, GH#7076
        d = vals.view("i8").astype(object)
    else:
        d = vals.astype(object)

    assert isinstance(d, np.ndarray), type(d)

    if ser._can_hold_na:
        # Note: this will miss timedeltas since they are converted to int
        mask = isna(d)
        d[mask] = None

    data_list[i] = d

exit((column_names, data_list))
