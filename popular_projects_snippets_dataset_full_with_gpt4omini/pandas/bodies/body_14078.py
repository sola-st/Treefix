# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
#  GH 2850
df = DataFrame(
    {
        "id1": {0: "1a3", 1: "9h4"},
        "id2": {0: np.nan, 1: "d67"},
        "id3": {0: "78d", 1: "79d"},
        "value": {0: 123, 1: 64},
    }
)

# multi-index
y = df.set_index(["id1", "id2", "id3"])
result = y.to_string()
expected = (
    "             value\nid1 id2 id3       \n"
    "1a3 NaN 78d    123\n9h4 d67 79d     64"
)
assert result == expected

# index
y = df.set_index("id2")
result = y.to_string()
expected = (
    "     id1  id3  value\nid2                 \n"
    "NaN  1a3  78d    123\nd67  9h4  79d     64"
)
assert result == expected

# with append (this failed in 0.12)
y = df.set_index(["id1", "id2"]).set_index("id3", append=True)
result = y.to_string()
expected = (
    "             value\nid1 id2 id3       \n"
    "1a3 NaN 78d    123\n9h4 d67 79d     64"
)
assert result == expected

# all-nan in mi
df2 = df.copy()
df2.loc[:, "id2"] = np.nan
y = df2.set_index("id2")
result = y.to_string()
expected = (
    "     id1  id3  value\nid2                 \n"
    "NaN  1a3  78d    123\nNaN  9h4  79d     64"
)
assert result == expected

# partial nan in mi
df2 = df.copy()
df2.loc[:, "id2"] = np.nan
y = df2.set_index(["id2", "id3"])
result = y.to_string()
expected = (
    "         id1  value\nid2 id3            \n"
    "NaN 78d  1a3    123\n    79d  9h4     64"
)
assert result == expected

df = DataFrame(
    {
        "id1": {0: np.nan, 1: "9h4"},
        "id2": {0: np.nan, 1: "d67"},
        "id3": {0: np.nan, 1: "79d"},
        "value": {0: 123, 1: 64},
    }
)

y = df.set_index(["id1", "id2", "id3"])
result = y.to_string()
expected = (
    "             value\nid1 id2 id3       \n"
    "NaN NaN NaN    123\n9h4 d67 79d     64"
)
assert result == expected
