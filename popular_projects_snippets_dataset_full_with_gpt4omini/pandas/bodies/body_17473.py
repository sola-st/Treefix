# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
for k, v in _offset_map.items():
    if v is None:
        continue
    assert k == v.copy()
