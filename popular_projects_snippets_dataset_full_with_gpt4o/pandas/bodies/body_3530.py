# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = frame_of_index_cols
df.index.name = index_name

key = box(df["B"])
if box == list:
    # list of strings gets interpreted as list of keys
    msg = "['one', 'two', 'three', 'one', 'two']"
    with pytest.raises(KeyError, match=msg):
        df.set_index(key, drop=drop, append=append)
else:
    # np.array/list-of-list "forget" the name of B
    name_mi = getattr(key, "names", None)
    name = [getattr(key, "name", None)] if name_mi is None else name_mi

    result = df.set_index(key, drop=drop, append=append)

    # only valid column keys are dropped
    # since B is always passed as array above, nothing is dropped
    expected = df.set_index(["B"], drop=False, append=append)
    expected.index.names = [index_name] + name if append else name

    tm.assert_frame_equal(result, expected)
