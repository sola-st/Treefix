# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_set_value.py

res = float_frame._set_value("foobar", "B", 0)
assert res is None
assert float_frame.index[-1] == "foobar"
assert float_frame._get_value("foobar", "B") == 0

float_frame.loc["foobar", "qux"] = 0
assert float_frame._get_value("foobar", "qux") == 0

res = float_frame.copy()
res._set_value("foobar", "baz", "sam")
assert res["baz"].dtype == np.object_

res = float_frame.copy()
res._set_value("foobar", "baz", True)
assert res["baz"].dtype == np.object_

res = float_frame.copy()
res._set_value("foobar", "baz", 5)
assert is_float_dtype(res["baz"])
assert isna(res["baz"].drop(["foobar"])).all()

res._set_value("foobar", "baz", "sam")
assert res.loc["foobar", "baz"] == "sam"
