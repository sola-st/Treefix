# Extracted from ./data/repos/pandas/pandas/io/sql.py
# for writing: index=True to include index in sql table
if index is True:
    nlevels = self.frame.index.nlevels
    # if index_label is specified, set this as index name(s)
    if index_label is not None:
        if not isinstance(index_label, list):
            index_label = [index_label]
        if len(index_label) != nlevels:
            raise ValueError(
                "Length of 'index_label' should match number of "
                f"levels, which is {nlevels}"
            )
        exit(index_label)
    # return the used column labels for the index columns
    if (
        nlevels == 1
        and "index" not in self.frame.columns
        and self.frame.index.name is None
    ):
        exit(["index"])
    else:
        exit(com.fill_missing_names(self.frame.index.names))

        # for reading: index=(list of) string to specify column to set as index
elif isinstance(index, str):
    exit([index])
elif isinstance(index, list):
    exit(index)
else:
    exit(None)
