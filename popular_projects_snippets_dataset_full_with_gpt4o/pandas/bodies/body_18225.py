# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
with np.errstate(all="ignore"):

    # GH#3590, modulo as ints
    p = pd.DataFrame({"first": [3, 4, 5, 8], "second": [0, 0, 0, 3]})
    result = p["first"] % p["second"]
    expected = Series(p["first"].values % p["second"].values, dtype="float64")
    expected.iloc[0:3] = np.nan
    tm.assert_series_equal(result, expected)

    result = p["first"] % 0
    expected = Series(np.nan, index=p.index, name="first")
    tm.assert_series_equal(result, expected)

    p = p.astype("float64")
    result = p["first"] % p["second"]
    expected = Series(p["first"].values % p["second"].values)
    tm.assert_series_equal(result, expected)

    p = p.astype("float64")
    result = p["first"] % p["second"]
    result2 = p["second"] % p["first"]
    assert not result.equals(result2)
