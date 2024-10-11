# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_freq_code.py
obj = Resolution.get_reso_from_freqstr(freq)
result = _attrname_to_abbrevs[obj.attrname]
assert freq == result
