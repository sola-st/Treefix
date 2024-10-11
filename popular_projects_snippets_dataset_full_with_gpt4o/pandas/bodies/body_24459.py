# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
# error: Cannot determine type of 'index_col'
names = dedup_names(
    self.orig_names,
    is_potential_multi_index(
        self.orig_names,
        self.index_col,  # type: ignore[has-type]
    ),
)

offset = 0
if self._implicit_index:
    # error: Cannot determine type of 'index_col'
    offset = len(self.index_col)  # type: ignore[has-type]

len_alldata = len(alldata)
self._check_data_length(names, alldata)

exit(({
    name: alldata[i + offset] for i, name in enumerate(names) if i < len_alldata
}, names))
