# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# check that the metadata matches up on the resulting ops

o = construct(frame_or_series, shape=3)
o.name = "foo"
o2 = construct(frame_or_series, shape=3)
o2.name = "bar"

# ----------
# preserving
# ----------

# simple ops with scalars
for op in ["__add__", "__sub__", "__truediv__", "__mul__"]:
    result = getattr(o, op)(1)
    tm.assert_metadata_equivalent(o, result)

# ops with like
for op in ["__add__", "__sub__", "__truediv__", "__mul__"]:
    result = getattr(o, op)(o)
    tm.assert_metadata_equivalent(o, result)

# simple boolean
for op in ["__eq__", "__le__", "__ge__"]:
    v1 = getattr(o, op)(o)
    tm.assert_metadata_equivalent(o, v1)
    tm.assert_metadata_equivalent(o, v1 & v1)
    tm.assert_metadata_equivalent(o, v1 | v1)

# combine_first
result = o.combine_first(o2)
tm.assert_metadata_equivalent(o, result)

# ---------------------------
# non-preserving (by default)
# ---------------------------

# add non-like
result = o + o2
tm.assert_metadata_equivalent(result)

# simple boolean
for op in ["__eq__", "__le__", "__ge__"]:

    # this is a name matching op
    v1 = getattr(o, op)(o)
    v2 = getattr(o, op)(o2)
    tm.assert_metadata_equivalent(v2)
    tm.assert_metadata_equivalent(v1 & v2)
    tm.assert_metadata_equivalent(v1 | v2)
