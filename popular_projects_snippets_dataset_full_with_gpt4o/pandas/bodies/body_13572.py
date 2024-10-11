# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
iterator = table_builder._create_row_iterator(over="body")
assert isinstance(iterator, RowBodyIterator)
