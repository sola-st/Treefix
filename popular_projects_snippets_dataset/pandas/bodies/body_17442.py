# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
offset = _create_offset(offset_types)

freqstr = offset.freqstr
if freqstr not in ("<Easter>", "<DateOffset: days=1>", "LWOM-SAT"):
    code = _get_offset(freqstr)
    assert offset.rule_code == code
