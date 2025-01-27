# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 15354
df = DataFrame(
    np.arange(10),
    index=date_range("2015-12-24", periods=10, freq="D"),
)
with pytest.raises(
    NotImplementedError, match="step is not supported with frequency windows"
):
    df.rolling("3D", step=3)
