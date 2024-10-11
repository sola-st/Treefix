# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_size.py
df = DataFrame(np.random.choice(20, (1000, 3)), columns=list("ABC"))
left = df.groupby(by=by, sort=sort).size()
right = df.groupby(by=by, sort=sort)["C"].apply(lambda a: a.shape[0])
tm.assert_series_equal(left, right, check_names=False)
