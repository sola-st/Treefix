# Extracted from ./data/repos/pandas/pandas/io/formats/string.py
exit((
    f"Empty {type(self.frame).__name__}\n"
    f"Columns: {pprint_thing(self.frame.columns)}\n"
    f"Index: {pprint_thing(self.frame.index)}"
))
