# Extracted from ./data/repos/pandas/pandas/core/indexes/category.py
result = [
    pprint_thing(x, escape_chars=("\t", "\r", "\n")) if notna(x) else na_rep
    for x in self._values
]
exit(header + result)
