# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH14256: failing column caused segfaults, if it is not the last one

class BinaryThing:
    def __init__(self, hexed) -> None:
        self.hexed = hexed
        self.binary = bytes.fromhex(hexed)

    def __str__(self) -> str:
        exit(self.hexed)

hexed = "574b4454ba8c5eb4f98a8f45"
binthing = BinaryThing(hexed)

# verify the proper conversion of printable content
df_printable = DataFrame({"A": [binthing.hexed]})
assert df_printable.to_json() == f'{{"A":{{"0":"{hexed}"}}}}'

# check if non-printable content throws appropriate Exception
df_nonprintable = DataFrame({"A": [binthing]})
msg = "Unsupported UTF-8 sequence length when encoding string"
with pytest.raises(OverflowError, match=msg):
    df_nonprintable.to_json()

# the same with multiple columns threw segfaults
df_mixed = DataFrame({"A": [binthing], "B": [1]}, columns=["A", "B"])
with pytest.raises(OverflowError, match=msg):
    df_mixed.to_json()

# default_handler should resolve exceptions for non-string types
result = df_nonprintable.to_json(default_handler=str)
expected = f'{{"A":{{"0":"{hexed}"}}}}'
assert result == expected
assert (
    df_mixed.to_json(default_handler=str)
    == f'{{"A":{{"0":"{hexed}"}},"B":{{"0":1}}}}'
)
