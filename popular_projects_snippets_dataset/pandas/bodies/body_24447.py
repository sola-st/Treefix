# Extracted from ./data/repos/pandas/pandas/io/parsers/c_parser_wrapper.py
# close handles opened by C parser
try:
    self._reader.close()
except ValueError:
    pass
