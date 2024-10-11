# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
if kwd == "millisecond":
    request.node.add_marker(
        pytest.mark.xfail(
            raises=NotImplementedError,
            reason="Constructing DateOffset object with `millisecond` is not "
            "yet supported.",
        )
    )
offset = DateOffset(**{kwd: 2})
assert offset.kwds == {kwd: 2}
assert getattr(offset, kwd) == 2
