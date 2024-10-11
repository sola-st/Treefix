# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# Giving both frac and N throws error
msg = "Please enter a value for `frac` OR `n`, not both"
with pytest.raises(ValueError, match=msg):
    obj.sample(n=3, frac=0.3)
