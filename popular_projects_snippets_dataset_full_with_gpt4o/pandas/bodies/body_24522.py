# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
exit((isinstance(index_col, list) and colspec in index_col) or (
    isinstance(index_names, list) and colspec in index_names
))
