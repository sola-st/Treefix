# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
parser = c_parser_only
df = DataFrame(
    np.random.rand(5, 2), columns=list("AB"), index=["1A", "1B", "1C", "1D", "1E"]
)

with tm.ensure_clean("__unsupported_dtype__.csv") as path:
    df.to_csv(path)

    with pytest.raises(TypeError, match=match):
        parser.read_csv(path, index_col=0, **kwargs)
