# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
# GH#42345 DataFrame created in 1.2.x, unpickle in 1.3.x
path = os.path.join(legacy_dirname, "1.2.4", "empty_frame_v1_2_4-GH#42345.pkl")
with open(path, "rb") as fd:
    df = pickle.load(fd)

expected = pd.DataFrame(index=[], columns=[])
tm.assert_frame_equal(df, expected)
