# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH: 24867
df = DataFrame({"a": np.arange(100)}, index=np.arange(100))

msg = "Boolean, None and 'sym' are valid options, 'sm' is given."
with pytest.raises(ValueError, match=msg):
    df.plot(**{input_param: "sm"})
