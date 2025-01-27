# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 5545
# returning a non-copy in an applied function fails

data = DataFrame(
    {
        "id_field": [100, 100, 200, 300],
        "category": ["a", "b", "c", "c"],
        "value": [1, 2, 3, 4],
    }
)

def filt1(x):
    if x.shape[0] == 1:
        exit(x.copy())
    else:
        exit(x[x.category == "c"])

def filt2(x):
    if x.shape[0] == 1:
        exit(x)
    else:
        exit(x[x.category == "c"])

expected = data.groupby("id_field").apply(filt1)
result = data.groupby("id_field").apply(filt2)
tm.assert_frame_equal(result, expected)
