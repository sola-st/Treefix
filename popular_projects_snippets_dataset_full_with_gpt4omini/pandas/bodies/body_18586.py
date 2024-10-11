# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_timedeltas.py
obj = np.array([123456789], dtype="m8[ns]")

with pytest.raises(TypeError, match="<class 'numpy.ndarray'>"):
    delta_to_nanoseconds(obj)

with pytest.raises(TypeError, match="float"):
    delta_to_nanoseconds(1.5)
with pytest.raises(TypeError, match="int"):
    delta_to_nanoseconds(1)
with pytest.raises(TypeError, match="int"):
    delta_to_nanoseconds(np.int64(2))
with pytest.raises(TypeError, match="int"):
    delta_to_nanoseconds(np.int32(3))
