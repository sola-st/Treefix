# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py

self.names = kwds.get("names")
self.orig_names: list | None = None

self.index_col = kwds.get("index_col", None)
self.unnamed_cols: set = set()
self.index_names: Sequence[Hashable] | None = None
self.col_names = None

self.parse_dates = _validate_parse_dates_arg(kwds.pop("parse_dates", False))
self._parse_date_cols: Iterable = []
self.date_parser = kwds.pop("date_parser", None)
self.dayfirst = kwds.pop("dayfirst", False)
self.keep_date_col = kwds.pop("keep_date_col", False)

self.na_values = kwds.get("na_values")
self.na_fvalues = kwds.get("na_fvalues")
self.na_filter = kwds.get("na_filter", False)
self.keep_default_na = kwds.get("keep_default_na", True)

self.dtype = copy(kwds.get("dtype", None))
self.converters = kwds.get("converters")
self.use_nullable_dtypes = kwds.get("use_nullable_dtypes", False)

self.true_values = kwds.get("true_values")
self.false_values = kwds.get("false_values")
self.cache_dates = kwds.pop("cache_dates", True)

self._date_conv = _make_date_converter(
    date_parser=self.date_parser,
    dayfirst=self.dayfirst,
    cache_dates=self.cache_dates,
)

# validate header options for mi
self.header = kwds.get("header")
if is_list_like(self.header, allow_sets=False):
    if kwds.get("usecols"):
        raise ValueError(
            "cannot specify usecols when specifying a multi-index header"
        )
    if kwds.get("names"):
        raise ValueError(
            "cannot specify names when specifying a multi-index header"
        )

    # validate index_col that only contains integers
    if self.index_col is not None:
        if not (
            is_list_like(self.index_col, allow_sets=False)
            and all(map(is_integer, self.index_col))
            or is_integer(self.index_col)
        ):
            raise ValueError(
                "index_col must only contain row numbers "
                "when specifying a multi-index header"
            )

self._name_processed = False

self._first_chunk = True

self.usecols, self.usecols_dtype = self._validate_usecols_arg(kwds["usecols"])

# Fallback to error to pass a sketchy test(test_override_set_noconvert_columns)
# Normally, this arg would get pre-processed earlier on
self.on_bad_lines = kwds.get("on_bad_lines", self.BadLineHandleMethod.ERROR)
