# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
double_input = 30.12345678901234567890
expected_exception = ValueError if isinstance(invalid_val, int) else TypeError
msg = (
    r"Invalid value '.*' for option 'double_precision', max is '15'|"
    r"an integer is required \(got type |"
    r"object cannot be interpreted as an integer"
)
with pytest.raises(expected_exception, match=msg):
    ujson.encode(double_input, double_precision=invalid_val)
