# Extracted from ./data/repos/pandas/pandas/tests/indexes/object/test_astype.py
# GH#45722 don't cast np.datetime64 NaTs to timedelta64 NaT
idx = Index([NaT.asm8] * 2, dtype=object)

msg = r"Invalid type for timedelta scalar: <class 'numpy.datetime64'>"
with pytest.raises(TypeError, match=msg):
    idx.astype("m8[ns]")
