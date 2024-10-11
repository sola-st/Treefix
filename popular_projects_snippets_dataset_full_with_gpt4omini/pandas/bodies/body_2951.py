# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
df = DataFrame(
    {
        0: [0, 0.5, 1.0, np.nan, 4, 8, np.nan, np.nan, 64],
        1: [1, 2, 3, 4, 3, 2, 1, 0, -1],
    }
)
df.interpolate(axis=0)
