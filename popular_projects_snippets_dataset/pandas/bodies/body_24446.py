# Extracted from ./data/repos/pandas/pandas/io/parsers/c_parser_wrapper.py
super().__init__(kwds)
self.kwds = kwds
kwds = kwds.copy()

self.low_memory = kwds.pop("low_memory", False)

# #2442
# error: Cannot determine type of 'index_col'
kwds["allow_leading_cols"] = (
    self.index_col is not False  # type: ignore[has-type]
)

# GH20529, validate usecol arg before TextReader
kwds["usecols"] = self.usecols

# Have to pass int, would break tests using TextReader directly otherwise :(
kwds["on_bad_lines"] = self.on_bad_lines.value

for key in (
    "storage_options",
    "encoding",
    "memory_map",
    "compression",
):
    kwds.pop(key, None)

kwds["dtype"] = ensure_dtype_objs(kwds.get("dtype", None))
self._reader = parsers.TextReader(src, **kwds)

self.unnamed_cols = self._reader.unnamed_cols

# error: Cannot determine type of 'names'
passed_names = self.names is None  # type: ignore[has-type]

if self._reader.header is None:
    self.names = None
else:
    # error: Cannot determine type of 'names'
    # error: Cannot determine type of 'index_names'
    (
        self.names,  # type: ignore[has-type]
        self.index_names,
        self.col_names,
        passed_names,
    ) = self._extract_multi_indexer_columns(
        self._reader.header,
        self.index_names,  # type: ignore[has-type]
        passed_names,
    )

# error: Cannot determine type of 'names'
if self.names is None:  # type: ignore[has-type]
    # error: Cannot determine type of 'names'
    self.names = list(range(self._reader.table_width))  # type: ignore[has-type]

# gh-9755
#
# need to set orig_names here first
# so that proper indexing can be done
# with _set_noconvert_columns
#
# once names has been filtered, we will
# then set orig_names again to names
# error: Cannot determine type of 'names'
self.orig_names = self.names[:]  # type: ignore[has-type]

if self.usecols:
    usecols = self._evaluate_usecols(self.usecols, self.orig_names)

    # GH 14671
    # assert for mypy, orig_names is List or None, None would error in issubset
    assert self.orig_names is not None
    if self.usecols_dtype == "string" and not set(usecols).issubset(
        self.orig_names
    ):
        self._validate_usecols_names(usecols, self.orig_names)

    # error: Cannot determine type of 'names'
    if len(self.names) > len(usecols):  # type: ignore[has-type]
        # error: Cannot determine type of 'names'
        self.names = [  # type: ignore[has-type]
            n
            # error: Cannot determine type of 'names'
            for i, n in enumerate(self.names)  # type: ignore[has-type]
            if (i in usecols or n in usecols)
        ]

    # error: Cannot determine type of 'names'
    if len(self.names) < len(usecols):  # type: ignore[has-type]
        # error: Cannot determine type of 'names'
        self._validate_usecols_names(
            usecols,
            self.names,  # type: ignore[has-type]
        )

        # error: Cannot determine type of 'names'
self._validate_parse_dates_presence(self.names)  # type: ignore[has-type]
self._set_noconvert_columns()

# error: Cannot determine type of 'names'
self.orig_names = self.names  # type: ignore[has-type]

if not self._has_complex_date_col:
    # error: Cannot determine type of 'index_col'
    if self._reader.leading_cols == 0 and is_index_col(
        self.index_col  # type: ignore[has-type]
    ):

        self._name_processed = True
        (
            index_names,
            # error: Cannot determine type of 'names'
            self.names,  # type: ignore[has-type]
            self.index_col,
        ) = self._clean_index_names(
            # error: Cannot determine type of 'names'
            self.names,  # type: ignore[has-type]
            # error: Cannot determine type of 'index_col'
            self.index_col,  # type: ignore[has-type]
        )

        if self.index_names is None:
            self.index_names = index_names

    if self._reader.header is None and not passed_names:
        assert self.index_names is not None
        self.index_names = [None] * len(self.index_names)

self._implicit_index = self._reader.leading_cols > 0
