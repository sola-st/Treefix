# Extracted from ./data/repos/pandas/pandas/io/parsers/arrow_parser_wrapper.py
"""
        Validates keywords before passing to pyarrow.
        """
encoding: str | None = self.kwds.get("encoding")
self.encoding = "utf-8" if encoding is None else encoding

self.usecols, self.usecols_dtype = self._validate_usecols_arg(
    self.kwds["usecols"]
)
na_values = self.kwds["na_values"]
if isinstance(na_values, dict):
    raise ValueError(
        "The pyarrow engine doesn't support passing a dict for na_values"
    )
self.na_values = list(self.kwds["na_values"])
