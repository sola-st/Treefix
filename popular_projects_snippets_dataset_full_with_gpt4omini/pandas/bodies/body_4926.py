# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
s = Series(
    [Timestamp("20130101") + timedelta(seconds=i * i) for i in range(10)]
)
td = s.diff()

msg = "|".join(
    [
        f"reduction operation '{opname}' not allowed for this dtype",
        rf"cannot perform {opname} with type timedelta64\[ns\]",
        f"does not support reduction '{opname}'",
    ]
)

with pytest.raises(TypeError, match=msg):
    getattr(td, opname)()

with pytest.raises(TypeError, match=msg):
    getattr(td.to_frame(), opname)(numeric_only=False)
