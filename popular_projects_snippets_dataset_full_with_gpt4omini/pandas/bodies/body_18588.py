# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timedeltas.py
# GH 32402
assert delta_to_nanoseconds(Timedelta(1e10)) == 1e10
assert delta_to_nanoseconds(Timedelta(nanoseconds=1e10)) == 1e10
