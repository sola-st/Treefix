# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 8121
df = DataFrame([[(1,), (1, 2), (1,), (1, 2)]], index=["ids"]).T
gr = df.groupby("ids")
expected = DataFrame({"ids": [(1,), (1,)]}, index=[0, 2])
result = gr.get_group((1,))
tm.assert_frame_equal(result, expected)

dt = pd.to_datetime(["2010-01-01", "2010-01-02", "2010-01-01", "2010-01-02"])
df = DataFrame({"ids": [(x,) for x in dt]})
gr = df.groupby("ids")
result = gr.get_group(("2010-01-01",))
expected = DataFrame({"ids": [(dt[0],), (dt[0],)]}, index=[0, 2])
tm.assert_frame_equal(result, expected)
