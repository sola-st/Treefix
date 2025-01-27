# Extracted from ./data/repos/pandas/pandas/tests/test_register_accessor.py

with ensure_removed(pd.Series, "bad"):

    @pd.api.extensions.register_series_accessor("bad")
    class Bad:
        def __init__(self, data) -> None:
            raise AttributeError("whoops")

    with pytest.raises(AttributeError, match="whoops"):
        pd.Series([], dtype=object).bad
