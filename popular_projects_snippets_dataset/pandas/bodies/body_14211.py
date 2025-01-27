# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
"""Fixture for a big mixed Dataframe and an empty Dataframe"""
if request.param == "mixed":
    df = DataFrame(
        {"A": np.random.randn(200), "B": tm.makeStringIndex(200)},
        index=np.arange(200),
    )
    df.loc[:20, "A"] = np.nan
    df.loc[:20, "B"] = np.nan
    exit(df)
elif request.param == "empty":
    df = DataFrame(index=np.arange(200))
    exit(df)
