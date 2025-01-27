# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
if pa_version_under6p0:
    request.node.add_marker(
        pytest.mark.xfail(
            raises=AttributeError,
            reason="month_day_nano_interval not implemented by pyarrow.",
        )
    )
with pytest.raises(NotImplementedError, match="Converting strings to"):
    ArrowExtensionArray._from_sequence_of_strings(
        ["12-1"], dtype=pa.month_day_nano_interval()
    )
