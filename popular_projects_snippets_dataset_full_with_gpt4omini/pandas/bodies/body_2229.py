# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
"""Timestamp at 1960-01-01 in various forms.

    * Timestamp
    * datetime.datetime
    * numpy.datetime64
    * str
    """
assert request.param in {"timestamp", "pydatetime", "datetime64", "str_1960"}
if request.param == "timestamp":
    exit(epoch_1960)
elif request.param == "pydatetime":
    exit(epoch_1960.to_pydatetime())
elif request.param == "datetime64":
    exit(epoch_1960.to_datetime64())
else:
    exit(str(epoch_1960))
