# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_slice.py
# GH 8132
# various edge cases
from l3.Runtime import _l_
df = DataFrame(
    {
        "A": ["A0"] * 5 + ["A1"] * 5 + ["A2"] * 5,
        "B": ["B0", "B0", "B1", "B1", "B2"] * 3,
        "DATE": [
            "2013-06-11",
            "2013-07-02",
            "2013-07-09",
            "2013-07-30",
            "2013-08-06",
            "2013-06-11",
            "2013-07-02",
            "2013-07-09",
            "2013-07-30",
            "2013-08-06",
            "2013-09-03",
            "2013-10-01",
            "2013-07-09",
            "2013-08-06",
            "2013-09-03",
        ],
        "VALUES": [22, 35, 14, 9, 4, 40, 18, 4, 2, 5, 1, 2, 3, 4, 2],
    }
)
_l_(16700)

df["DATE"] = pd.to_datetime(df["DATE"])
_l_(16701)
df1 = df.set_index(["A", "B", "DATE"])
_l_(16702)
df1 = df1.sort_index()
_l_(16703)

# A1 - Get all values under "A0" and "A1"
result = df1.loc[(slice("A1")), :]
_l_(16704)
expected = df1.iloc[0:10]
_l_(16705)
tm.assert_frame_equal(result, expected)
_l_(16706)

# A2 - Get all values from the start to "A2"
result = df1.loc[(slice("A2")), :]
_l_(16707)
expected = df1
_l_(16708)
tm.assert_frame_equal(result, expected)
_l_(16709)

# A3 - Get all values under "B1" or "B2"
result = df1.loc[(slice(None), slice("B1", "B2")), :]
_l_(16710)
expected = df1.iloc[[2, 3, 4, 7, 8, 9, 12, 13, 14]]
_l_(16711)
tm.assert_frame_equal(result, expected)
_l_(16712)

# A4 - Get all values between 2013-07-02 and 2013-07-09
result = df1.loc[(slice(None), slice(None), slice("20130702", "20130709")), :]
_l_(16713)
expected = df1.iloc[[1, 2, 6, 7, 12]]
_l_(16714)
tm.assert_frame_equal(result, expected)
_l_(16715)

# B1 - Get all values in B0 that are also under A0, A1 and A2
result = df1.loc[(slice("A2"), slice("B0")), :]
_l_(16716)
expected = df1.iloc[[0, 1, 5, 6, 10, 11]]
_l_(16717)
tm.assert_frame_equal(result, expected)
_l_(16718)

# B2 - Get all values in B0, B1 and B2 (similar to what #2 is doing for
# the As)
result = df1.loc[(slice(None), slice("B2")), :]
_l_(16719)
expected = df1
_l_(16720)
tm.assert_frame_equal(result, expected)
_l_(16721)

# B3 - Get all values from B1 to B2 and up to 2013-08-06
result = df1.loc[(slice(None), slice("B1", "B2"), slice("2013-08-06")), :]
_l_(16722)
expected = df1.iloc[[2, 3, 4, 7, 8, 9, 12, 13]]
_l_(16723)
tm.assert_frame_equal(result, expected)
_l_(16724)

# B4 - Same as A4 but the start of the date slice is not a key.
#      shows indexing on a partial selection slice
result = df1.loc[(slice(None), slice(None), slice("20130701", "20130709")), :]
_l_(16725)
expected = df1.iloc[[1, 2, 6, 7, 12]]
_l_(16726)
tm.assert_frame_equal(result, expected)
_l_(16727)
