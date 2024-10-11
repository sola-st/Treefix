# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# gh-10444, GH32590
df = DataFrame(
    {
        "a": np.random.rand(10),
        "b": np.random.randint(0, 10, 10),
        "c": to_datetime(
            np.random.randint(
                1582800000000000000, 1583500000000000000, 10, dtype=np.int64
            )
        ),
        "d": to_datetime(
            np.random.randint(
                1582800000000000000, 1583500000000000000, 10, dtype=np.int64
            ),
            utc=True,
        ),
    }
)
df_o = df.astype(object)

msg = "hist method requires numerical or datetime columns, nothing to plot."
with pytest.raises(ValueError, match=msg):
    df_o.hist()
