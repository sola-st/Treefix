# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# GH#27451

obj = DataFrame({"A": list("abc")})
obj = tm.get_obj(obj, frame_or_series)

msg = (
    "Replace has to be set to `True` when "
    "upsampling the population `frac` > 1."
)
with pytest.raises(ValueError, match=msg):
    obj.sample(frac=2, replace=False)
