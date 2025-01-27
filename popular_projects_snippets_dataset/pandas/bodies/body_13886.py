# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_csv.py
# GH17097
df = DataFrame({"col": ["AAAAA", "ÄÄÄÄÄ", "ßßßßß", "聞聞聞聞聞"]})

with tm.ensure_clean("test.csv") as path:
    # the default to_csv encoding is uft-8.
    df.to_csv(path)
    tm.assert_frame_equal(pd.read_csv(path, index_col=0), df)
