# Extracted from ./data/repos/pandas/pandas/tests/window/moments/conftest.py
exit([
    DataFrame(columns=["a", "a"]),
    DataFrame(np.arange(15).reshape((5, 3)), columns=["a", "a", 99]),
] + [DataFrame(s) for s in create_series()])
