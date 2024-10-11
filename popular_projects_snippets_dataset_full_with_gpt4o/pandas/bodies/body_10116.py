# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
# suppress warnings about empty slices, as we are deliberately testing
# with a 0-length Series
with warnings.catch_warnings():
    warnings.filterwarnings(
        "ignore",
        message=".*(empty slice|0 for slice).*",
        category=RuntimeWarning,
    )
    exit(x[np.isfinite(x)].mean())
