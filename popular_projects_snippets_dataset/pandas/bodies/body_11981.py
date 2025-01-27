# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
msg = "not all elements from date_cols are numpy arrays"
value = "19990127"

date_cols = tuple(container([value]) for _ in range(dim))

with pytest.raises(ValueError, match=msg):
    parsing.concat_date_cols(date_cols)
