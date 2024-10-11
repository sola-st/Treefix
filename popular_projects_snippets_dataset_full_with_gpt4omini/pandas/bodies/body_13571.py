# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
iterator = table_builder._create_row_iterator(over="header")
assert isinstance(iterator, RowHeaderIterator)
