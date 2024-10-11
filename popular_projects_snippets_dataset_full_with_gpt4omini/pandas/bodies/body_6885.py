# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
with pytest.raises(ValueError, match=f"invalid na_position: {na_position}"):
    with tm.maybe_produces_warning(
        PerformanceWarning,
        getattr(index_with_missing.dtype, "storage", "") == "pyarrow",
        check_stacklevel=False,
    ):
        index_with_missing.sort_values(na_position=na_position)
