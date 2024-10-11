# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 9464
with tm.assert_produces_warning(None):
    df = DataFrame(np.random.randn(100, 4))
    df.plot(subplots=True, layout=(3, 2))

    df = DataFrame(
        np.random.randn(100, 4), index=date_range("1/1/2000", periods=100)
    )
    df.plot(subplots=True, layout=(3, 2))
