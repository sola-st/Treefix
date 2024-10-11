# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pipe.py
obj = DataFrame({"A": [1, 2, 3]})
obj = tm.get_obj(obj, frame_or_series)

f = lambda x, y: y

msg = "y is both the pipe target and a keyword argument"

with pytest.raises(ValueError, match=msg):
    obj.pipe((f, "y"), x=1, y=0)
