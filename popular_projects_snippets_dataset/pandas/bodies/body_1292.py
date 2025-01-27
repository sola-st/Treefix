# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
# GH#3970
with option_context("chained_assignment", None):
    df = DataFrame({"aa": range(5), "bb": [2.2] * 5})
    df["cc"] = 0.0

    ck = [True] * len(df)

    df["bb"].iloc[0] = 0.13

    # GH#3970 this lookup used to break the chained setting to 0.15
    df.iloc[ck]

    df["bb"].iloc[0] = 0.15
    if not using_copy_on_write:
        assert df["bb"].iloc[0] == 0.15
    else:
        assert df["bb"].iloc[0] == 2.2
