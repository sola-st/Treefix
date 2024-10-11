# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
lst = ["M", "MS", "BM", "BMS", "D", "B", "H", "T", "S", "L", "U"]
for k in lst:
    assert k == _get_offset(k).rule_code
    # should be cached - this is kind of an internals test...
    assert k in _offset_map
    assert k == (_get_offset(k) * 3).rule_code

suffix_lst = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
base = "W"
for v in suffix_lst:
    alias = "-".join([base, v])
    assert alias == _get_offset(alias).rule_code
    assert alias == (_get_offset(alias) * 5).rule_code

suffix_lst = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
]
base_lst = ["A", "AS", "BA", "BAS", "Q", "QS", "BQ", "BQS"]
for base in base_lst:
    for v in suffix_lst:
        alias = "-".join([base, v])
        assert alias == _get_offset(alias).rule_code
        assert alias == (_get_offset(alias) * 5).rule_code
