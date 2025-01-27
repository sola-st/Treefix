# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 20636
index = IntervalIndex.from_breaks(breaks1)
key = make_key(breaks2)

msg = (
    f"Cannot index an IntervalIndex of subtype {breaks1.dtype} with "
    f"values of dtype {breaks2.dtype}"
)
msg = re.escape(msg)
with pytest.raises(ValueError, match=msg):
    index._maybe_convert_i8(key)
