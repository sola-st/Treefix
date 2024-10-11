# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH 21982

obj = DataFrame(np.arange(100).reshape(10, 10))
obj = tm.get_obj(obj, frame_or_series)

with pytest.raises(TypeError, match="Cannot index by location index"):
    obj.iloc["a"]
