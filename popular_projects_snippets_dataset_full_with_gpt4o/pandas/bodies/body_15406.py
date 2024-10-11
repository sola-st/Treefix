# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#14359: test that you cannot mutate a read only buffer

array = np.zeros(5)
array.flags.writeable = False  # make the array immutable
series = Series(array)

for n in series.index:
    msg = "assignment destination is read-only"
    with pytest.raises(ValueError, match=msg):
        series[n] = 1

    assert array[n] == 0
