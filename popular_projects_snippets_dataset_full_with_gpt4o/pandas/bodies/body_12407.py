# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
pytest.importorskip(module)
path = datapath(*path)

mypath = CustomFSPath(path)
result = reader(mypath)
expected = reader(path)

if path.endswith(".pickle"):
    # categorical
    tm.assert_categorical_equal(result, expected)
else:
    tm.assert_frame_equal(result, expected)
