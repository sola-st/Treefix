# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
# pickle file written with py27, should be readable without raising
#  UnicodeDecodeError, see GH#28645 and GH#31988
path = datapath("io", "data", "pickle", pickle_file)
df = pd.read_pickle(path)

# just test the columns are correct since the values are random
tm.assert_index_equal(df.columns, excols)
