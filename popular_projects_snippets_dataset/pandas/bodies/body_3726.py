# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_describe.py
# GH#26660
df = DataFrame({"x": [1]})
pct = np.linspace(0, 1, 10 + 1)
result = df.describe(percentiles=pct)

expected = DataFrame(
    {"x": [1.0, 1.0, np.NaN, 1.0, *(1.0 for _ in pct), 1.0]},
    index=[
        "count",
        "mean",
        "std",
        "min",
        "0%",
        "10%",
        "20%",
        "30%",
        "40%",
        "50%",
        "60%",
        "70%",
        "80%",
        "90%",
        "100%",
        "max",
    ],
)
tm.assert_frame_equal(result, expected)
