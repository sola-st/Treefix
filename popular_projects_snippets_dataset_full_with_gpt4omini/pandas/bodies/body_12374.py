# Extracted from ./data/repos/pandas/pandas/tests/io/test_spss.py
# test file from the Haven project (https://haven.tidyverse.org/)
fname = datapath("io", "data", "spss", "labelled-str.sav")

df = pd.read_spss(fname, convert_categoricals=True)
expected = pd.DataFrame({"gender": ["Male", "Female"]})
expected["gender"] = pd.Categorical(expected["gender"])
tm.assert_frame_equal(df, expected)

df = pd.read_spss(fname, convert_categoricals=False)
expected = pd.DataFrame({"gender": ["M", "F"]})
tm.assert_frame_equal(df, expected)
