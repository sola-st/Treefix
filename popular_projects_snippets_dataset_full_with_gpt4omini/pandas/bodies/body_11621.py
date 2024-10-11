# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
# see gh-10153
parser = all_parsers
data = """a,b
1,a
1,b
1,b
2,c"""
cats = ["a", "b", "c"]
expecteds = [
    DataFrame({"a": [1, 1], "b": Categorical(["a", "b"], categories=cats)}),
    DataFrame(
        {"a": [1, 2], "b": Categorical(["b", "c"], categories=cats)},
        index=[2, 3],
    ),
]
dtype = CategoricalDtype(cats)
with parser.read_csv(StringIO(data), dtype={"b": dtype}, chunksize=2) as actuals:
    for actual, expected in zip(actuals, expecteds):
        tm.assert_frame_equal(actual, expected)
