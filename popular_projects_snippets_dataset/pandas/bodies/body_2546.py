# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#35369
df = DataFrame({"h": Series(list("mn")).astype("category")})
df.h = df.h.cat.reorder_categories(["n", "m"])
expected = DataFrame(
    {"h": Categorical(["m", "n"]).reorder_categories(["n", "m"])}
)
tm.assert_frame_equal(df, expected)
