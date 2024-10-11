# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py
# GH 24025
df = pd.DataFrame(
    {
        "col1": list("abc"),
        "col2": list(range(1, 4)),
        "col3": list("xyz"),
        "col4": list(range(4, 7)),
    }
)
columns = ["col1", "col3"]
self.check_round_trip(df, expected=df[columns], columns=columns)
