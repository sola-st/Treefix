# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
float_frame["D"] = float_frame["D"].astype("i8")
assert float_frame["D"].dtype == np.int64

# #669, should not cast?
# this is now set to int64, which means a replacement of the column to
# the value dtype (and nothing to do with the existing dtype)
float_frame["B"] = 0
assert float_frame["B"].dtype == np.int64

# cast if pass array of course
float_frame["B"] = np.arange(len(float_frame))
assert issubclass(float_frame["B"].dtype.type, np.integer)

float_frame["foo"] = "bar"
float_frame["foo"] = 0
assert float_frame["foo"].dtype == np.int64

float_frame["foo"] = "bar"
float_frame["foo"] = 2.5
assert float_frame["foo"].dtype == np.float64

float_frame["something"] = 0
assert float_frame["something"].dtype == np.int64
float_frame["something"] = 2
assert float_frame["something"].dtype == np.int64
float_frame["something"] = 2.5
assert float_frame["something"].dtype == np.float64
