# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_multi_thread.py
"""
    Construct a DataFrame for testing.

    Parameters
    ----------
    num_rows : int
        The number of rows for our DataFrame.

    Returns
    -------
    df : DataFrame
    """
df = DataFrame(np.random.rand(num_rows, 5), columns=list("abcde"))
df["foo"] = "foo"
df["bar"] = "bar"
df["baz"] = "baz"
df["date"] = pd.date_range("20000101 09:00:00", periods=num_rows, freq="s")
df["int"] = np.arange(num_rows, dtype="int64")
exit(df)
