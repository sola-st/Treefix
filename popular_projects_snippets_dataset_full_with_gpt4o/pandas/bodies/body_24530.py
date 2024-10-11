# Extracted from ./data/repos/pandas/pandas/io/parsers/arrow_parser_wrapper.py
"""
        Rename some arguments to pass to pyarrow
        """
mapping = {
    "usecols": "include_columns",
    "na_values": "null_values",
    "escapechar": "escape_char",
    "skip_blank_lines": "ignore_empty_lines",
}
for pandas_name, pyarrow_name in mapping.items():
    if pandas_name in self.kwds and self.kwds.get(pandas_name) is not None:
        self.kwds[pyarrow_name] = self.kwds.pop(pandas_name)

self.parse_options = {
    option_name: option_value
    for option_name, option_value in self.kwds.items()
    if option_value is not None
    and option_name
    in ("delimiter", "quote_char", "escape_char", "ignore_empty_lines")
}
self.convert_options = {
    option_name: option_value
    for option_name, option_value in self.kwds.items()
    if option_value is not None
    and option_name
    in ("include_columns", "null_values", "true_values", "false_values")
}
self.read_options = {
    "autogenerate_column_names": self.header is None,
    "skip_rows": self.header
    if self.header is not None
    else self.kwds["skiprows"],
}
