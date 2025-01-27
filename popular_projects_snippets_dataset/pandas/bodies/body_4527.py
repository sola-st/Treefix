# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#46822
msg = "Empty data passed with indices specified."
with pytest.raises(ValueError, match=msg):
    DataFrame(data=np.array([]), columns=["a", "b"])
