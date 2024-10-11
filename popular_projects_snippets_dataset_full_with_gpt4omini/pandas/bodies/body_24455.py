# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
"""
        Workhorse function for processing nested list into DataFrame
        """
super().__init__(kwds)

self.data: Iterator[str] | None = None
self.buf: list = []
self.pos = 0
self.line_pos = 0

self.skiprows = kwds["skiprows"]

if callable(self.skiprows):
    self.skipfunc = self.skiprows
else:
    self.skipfunc = lambda x: x in self.skiprows

self.skipfooter = _validate_skipfooter_arg(kwds["skipfooter"])
self.delimiter = kwds["delimiter"]

self.quotechar = kwds["quotechar"]
if isinstance(self.quotechar, str):
    self.quotechar = str(self.quotechar)

self.escapechar = kwds["escapechar"]
self.doublequote = kwds["doublequote"]
self.skipinitialspace = kwds["skipinitialspace"]
self.lineterminator = kwds["lineterminator"]
self.quoting = kwds["quoting"]
self.skip_blank_lines = kwds["skip_blank_lines"]

self.names_passed = kwds["names"] or None

self.has_index_names = False
if "has_index_names" in kwds:
    self.has_index_names = kwds["has_index_names"]

self.verbose = kwds["verbose"]

self.thousands = kwds["thousands"]
self.decimal = kwds["decimal"]

self.comment = kwds["comment"]

# Set self.data to something that can read lines.
if isinstance(f, list):
    # read_excel: f is a list
    self.data = cast(Iterator[str], f)
else:
    assert hasattr(f, "readline")
    self._make_reader(f)

# Get columns in two steps: infer from data, then
# infer column indices from self.usecols if it is specified.
self._col_indices: list[int] | None = None
columns: list[list[Scalar | None]]
(
    columns,
    self.num_original_columns,
    self.unnamed_cols,
) = self._infer_columns()

# Now self.columns has the set of columns that we will process.
# The original set is stored in self.original_columns.
# error: Cannot determine type of 'index_names'
self.columns: list[Hashable]
(
    self.columns,
    self.index_names,
    self.col_names,
    _,
) = self._extract_multi_indexer_columns(
    columns,
    self.index_names,  # type: ignore[has-type]
)

# get popped off for index
self.orig_names: list[Hashable] = list(self.columns)

# needs to be cleaned/refactored
# multiple date column thing turning into a real spaghetti factory

if not self._has_complex_date_col:
    (index_names, self.orig_names, self.columns) = self._get_index_name(
        self.columns
    )
    self._name_processed = True
    if self.index_names is None:
        self.index_names = index_names

if self._col_indices is None:
    self._col_indices = list(range(len(self.columns)))

self._parse_date_cols = self._validate_parse_dates_presence(self.columns)
no_thousands_columns: set[int] | None = None
if self.parse_dates:
    no_thousands_columns = self._set_noconvert_dtype_columns(
        self._col_indices, self.columns
    )
self._no_thousands_columns = no_thousands_columns

if len(self.decimal) != 1:
    raise ValueError("Only length-1 decimal markers supported")

decimal = re.escape(self.decimal)
if self.thousands is None:
    regex = rf"^[\-\+]?[0-9]*({decimal}[0-9]*)?([0-9]?(E|e)\-?[0-9]+)?$"
else:
    thousands = re.escape(self.thousands)
    regex = (
        rf"^[\-\+]?([0-9]+{thousands}|[0-9])*({decimal}[0-9]*)?"
        rf"([0-9]?(E|e)\-?[0-9]+)?$"
    )
self.num = re.compile(regex)
