# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_update.py
df = DataFrame(
    [[1.5, 1, 3.0], [1.5, np.nan, 3.0], [1.5, np.nan, 3], [1.5, np.nan, 3]]
)

other = DataFrame([[2.0, np.nan], [np.nan, 7]], index=[1, 3], columns=[1, 2])
with pytest.raises(ValueError, match="Data overlaps"):
    df.update(other, errors="raise")
