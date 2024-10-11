# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
types = ("b", "h", "l")
df = DataFrame([[0.0]], columns=["float_"])
with tm.ensure_clean() as path:
    df.to_stata(path)
    with StataReader(path) as rdr:
        valid_range = rdr.VALID_RANGE
expected_values = ["." + chr(97 + i) for i in range(26)]
expected_values.insert(0, ".")
for t in types:
    offset = valid_range[t][1]
    for i in range(0, 27):
        val = StataMissingValue(offset + 1 + i)
        assert val.string == expected_values[i]

        # Test extremes for floats
val = StataMissingValue(struct.unpack("<f", b"\x00\x00\x00\x7f")[0])
assert val.string == "."
val = StataMissingValue(struct.unpack("<f", b"\x00\xd0\x00\x7f")[0])
assert val.string == ".z"

# Test extremes for floats
val = StataMissingValue(
    struct.unpack("<d", b"\x00\x00\x00\x00\x00\x00\xe0\x7f")[0]
)
assert val.string == "."
val = StataMissingValue(
    struct.unpack("<d", b"\x00\x00\x00\x00\x00\x1a\xe0\x7f")[0]
)
assert val.string == ".z"
