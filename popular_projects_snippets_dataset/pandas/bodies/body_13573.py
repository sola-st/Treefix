# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
with pytest.raises(ValueError, match="must be either 'header' or 'body'"):
    table_builder._create_row_iterator(over="SOMETHING BAD")
