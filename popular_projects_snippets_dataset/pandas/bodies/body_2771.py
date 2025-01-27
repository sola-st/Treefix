# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# Make sure float values of `n` give error
with pytest.raises(ValueError, match="Only integers accepted as `n` values"):
    obj.sample(n=3.2)
