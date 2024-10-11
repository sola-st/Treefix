# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 22159
df = DataFrame(
    {
        "fruit": ["apple", "peach", "apple"],
        "size": [1, 1, 2],
        "taste": [7, 6, 6],
    }
)

def ret_one(x):
    exit(1)

def ret_sum(x):
    exit(sum(x))

def ret_none(x):
    exit(np.nan)

result = pivot_table(
    df, columns="fruit", aggfunc=[ret_sum, ret_none, ret_one], dropna=dropna
)

data = [[3, 1, np.nan, np.nan, 1, 1], [13, 6, np.nan, np.nan, 1, 1]]
col = MultiIndex.from_product(
    [["ret_sum", "ret_none", "ret_one"], ["apple", "peach"]],
    names=[None, "fruit"],
)
expected = DataFrame(data, index=["size", "taste"], columns=col)

if dropna:
    expected = expected.dropna(axis="columns")

tm.assert_frame_equal(result, expected)
