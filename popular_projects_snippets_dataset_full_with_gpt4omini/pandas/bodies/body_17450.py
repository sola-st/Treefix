# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
off = _create_offset(offset_types)
res = tm.round_trip_pickle(off)
assert off == res
if type(off) is not DateOffset:
    for attr in off._attributes:
        if attr == "calendar":
            # np.busdaycalendar __eq__ will return False;
            #  we check holidays and weekmask attrs so are OK
            continue
        # Make sure nothings got lost from _params (which __eq__) is based on
        assert getattr(off, attr) == getattr(res, attr)
