# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 22984 ensure entire window is filled
terminal_size = (80, 24)
df = DataFrame(np.random.rand(1, 7))

monkeypatch.setattr(
    "pandas.io.formats.format.get_terminal_size", lambda: terminal_size
)
assert "..." not in str(df)
