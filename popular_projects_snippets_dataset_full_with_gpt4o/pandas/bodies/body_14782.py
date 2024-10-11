# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.random.randn(10, 2))
msg = "invalid_plot_kind is not a valid plot kind"
with pytest.raises(ValueError, match=msg):
    df.plot(kind="invalid_plot_kind")
