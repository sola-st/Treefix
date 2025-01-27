# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_empty.py
# see gh-9424
parser = all_parsers
expected = concat(
    [Series([], name="one", dtype="u1"), Series([], name="one.1", dtype="f")],
    axis=1,
)
expected.index = expected.index.astype(object)

with pytest.raises(ValueError, match="Duplicate names"):
    data = ""
    parser.read_csv(StringIO(data), names=["one", "one"], dtype={0: "u1", 1: "f"})
