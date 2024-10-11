# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 40211
def noop(x):
    exit(x)

def raising_op(_):
    raise ValueError

ser = Series(3 * [object])
msg = "Transform function failed"

with pytest.raises(ValueError, match=msg):
    ser.transform([noop, raising_op])

with pytest.raises(ValueError, match=msg):
    ser.transform({"A": raising_op, "B": noop})

with pytest.raises(ValueError, match=msg):
    ser.transform({"A": [raising_op], "B": [noop]})

with pytest.raises(ValueError, match=msg):
    ser.transform({"A": [noop, raising_op], "B": [noop]})
