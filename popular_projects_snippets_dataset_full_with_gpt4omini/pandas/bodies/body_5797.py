# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
with pytest.raises(NotImplementedError, match="Passing pyarrow type"):
    ArrowDtype.construct_from_string("timestamp[s, tz=UTC][pyarrow]")
