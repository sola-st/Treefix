# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
# see gh-2631
parser = all_parsers
data = """YEAR, DOY, a
2001,106380451,10
2001,,11
2001,106380451,67"""

msg = (
    "Integer column has NA values"
    if parser.engine == "c"
    else "Unable to convert column DOY"
)
with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), dtype={"DOY": np.int64}, skipinitialspace=True)
