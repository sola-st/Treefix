# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #41241
df = pd.DataFrame(
    {
        "value": pd.array([], dtype=dtype),
    }
)
# GH 45694
expected = None
if dtype == "float":
    expected = pd.DataFrame(
        {
            "value": pd.array([], dtype="Float64"),
        }
    )
check_round_trip(
    df, pa, read_kwargs={"use_nullable_dtypes": True}, expected=expected
)
