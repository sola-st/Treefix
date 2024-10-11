# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
if kwd == "millisecond":
    request.node.add_marker(
        pytest.mark.xfail(
            raises=NotImplementedError,
            reason="Constructing DateOffset object with `millisecond` is not "
            "yet supported.",
        )
    )
# Check that all the arguments specified in liboffsets._relativedelta_kwds
# are in fact valid relativedelta keyword args
DateOffset(**{kwd: 1})
