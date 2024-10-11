# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
parser = all_parsers
msg = (
    "(Bool column has NA values in column [0a])|"
    "(cannot safely convert passed user dtype of "
    "bool for object dtyped data in column 0)"
)
with pytest.raises(ValueError, match=msg):
    parser.read_csv(
        StringIO(data),
        header=None,
        names=["a", "b"],
        dtype={"a": "bool"},
        na_values=na_values,
    )
