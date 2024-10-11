# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_unsupported.py
# see gh-12935
data = "a b c\n1 2 3"

for engine in ("c", "python"):
    with pytest.raises(TypeError, match="unexpected keyword"):
        read_csv(StringIO(data), engine=engine, mangle_dupe_cols=True)
