# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
series = float_string_frame._series
for k, v in series.items():
    assert v.name == k
