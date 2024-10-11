# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
with pytest.raises(
    ValueError,
    match="A negative number of rows requested. Please provide `n` >= 0",
):
    obj.sample(n=-3)
with pytest.raises(
    ValueError,
    match="A negative number of rows requested. Please provide `frac` >= 0",
):
    obj.sample(frac=-0.3)
