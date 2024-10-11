# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
dfj2 = DataFrame(np.random.randn(5, 2), columns=list("AB"))
dfj2["date"] = Timestamp("20130101")
dfj2["ints"] = range(5)
dfj2["bools"] = True
dfj2.index = pd.date_range("20130101", periods=5)

json = dfj2.to_json()
result = read_json(json, dtype={"ints": np.int64, "bools": np.bool_})
tm.assert_frame_equal(result, result)
