# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
skip_if_no_pandas_parser(parser)
df = DataFrame(
    {
        "Symbol": ["BUD US", "BUD US", "IBM US", "IBM US"],
        "Price": [109.70, 109.72, 183.30, 183.35],
    }
)
e = df[df.Symbol == "BUD US"]
symb = "BUD US"  # noqa:F841
r = df.query("Symbol == @symb", parser=parser, engine=engine)
tm.assert_frame_equal(e, r)
