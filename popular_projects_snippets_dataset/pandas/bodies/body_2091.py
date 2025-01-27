# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# See GH#18666
with tm.set_timezone("US/Eastern"):
    # GH#18705
    now = Timestamp("now")
    pdnow = to_datetime("now")
    pdnow2 = to_datetime(["now"])[0]

    # These should all be equal with infinite perf; this gives
    # a generous margin of 10 seconds
    assert abs(pdnow.value - now.value) < 1e10
    assert abs(pdnow2.value - now.value) < 1e10

    assert pdnow.tzinfo is None
    assert pdnow2.tzinfo is None
