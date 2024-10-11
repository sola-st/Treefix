# Extracted from ./data/repos/pandas/pandas/io/pytables.py
if not append and self.is_exists:
    self._handle.remove_node(self.group, "table")

# create the axes
table = self._create_axes(
    axes=axes,
    obj=obj,
    validate=append,
    min_itemsize=min_itemsize,
    nan_rep=nan_rep,
    data_columns=data_columns,
)

for a in table.axes:
    a.validate_names()

if not table.is_exists:

    # create the table
    options = table.create_description(
        complib=complib,
        complevel=complevel,
        fletcher32=fletcher32,
        expectedrows=expectedrows,
    )

    # set the table attributes
    table.set_attrs()

    options["track_times"] = track_times

    # create the table
    table._handle.create_table(table.group, **options)

# update my info
table.attrs.info = table.info

# validate the axes and set the kinds
for a in table.axes:
    a.validate_and_set(table, append)

# add the rows
table.write_data(chunksize, dropna=dropna)
